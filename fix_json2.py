# -*- coding: utf-8 -*-
import json

with open(r'C:\ECNU-个人资料\复习资料\中国当代史\quiz-site\cr_50_new.json', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all positions of ASCII double quote (0x22)
# and classify if they are JSON structural or internal text quotes
positions = []
for i, ch in enumerate(content):
    if ch == '"':
        # Check context - is this a JSON structural quote or inside Chinese text?
        positions.append(i)

print(f"Total ASCII double quotes: {len(positions)}")

# Strategy: replace ALL internal non-JSON-structural quotes with Chinese quotes
# A JSON structural quote appears at:
# - Start/end of keys like "id", "period", etc.
# - Start/end of values
# - Array brackets: ["...", "..."]
# An internal quote appears within Chinese text

# Let's find internal quotes by looking at context
# Internal quote: preceded by Chinese char (U+4E00-U+9FFF etc.) or followed by Chinese char
import unicodedata

def is_cjk_or_punct(ch):
    cp = ord(ch)
    return (0x4E00 <= cp <= 0x9FFF or  # CJK Unified
            0x3400 <= cp <= 0x4DBF or  # CJK Extension A
            0x20000 <= cp <= 0x2A6DF or # CJK Extension B
            0x3000 <= cp <= 0x303F or  # CJK punctuation
            0xFF00 <= cp <= 0xFFEF or  # Halfwidth/Fullwidth
            0x2000 <= cp <= 0x206F or  # General punctuation
            ch in '，。、；：？！…—～')

internal_quotes = []
for pos in positions:
    # Check if this is likely an internal quote
    before = content[pos-1] if pos > 0 else ''
    after = content[pos+1] if pos < len(content)-1 else ''

    # JSON structural: before is whitespace/:/[/, or after is whitespace/:/,/]/}
    is_structural_before = before in ' \t\n\r:[,{'
    is_structural_after = after in ' \t\n\r:],}'

    if before == '\\':
        continue  # Already escaped

    if not (is_structural_before or is_structural_after):
        # Could be internal
        internal_quotes.append(pos)

print(f"Likely internal quotes: {len(internal_quotes)}")

# Now replace internal quotes with Chinese quotation marks
# Even-numbered occurrences (0,2,4...) -> opening quote "
# Odd-numbered occurrences (1,3,5...) -> closing quote "
internal_quotes.sort()
chars = list(content)
for j, pos in enumerate(internal_quotes):
    if j % 2 == 0:
        chars[pos] = '“'  # LEFT DOUBLE QUOTATION MARK
    else:
        chars[pos] = '”'  # RIGHT DOUBLE QUOTATION MARK

new_content = ''.join(chars)

# Verify
with open(r'C:\ECNU-个人资料\复习资料\中国当代史\quiz-site\cr_50_new.json', 'w', encoding='utf-8') as f:
    f.write(new_content)

try:
    data = json.loads(new_content)
    print(f'SUCCESS! JSON valid with {len(data)} questions')
    for i, q in enumerate(data):
        print(f'  Q{i+1} ({q["id"]}): Q={len(q["question"])} chars, A={len(q["analysis"])} chars')
except json.JSONDecodeError as e:
    print(f'Still invalid at pos {e.pos}: {e}')
    print(f'Context: {new_content[e.pos-40:e.pos+40]}')
