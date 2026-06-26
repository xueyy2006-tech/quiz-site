# -*- coding: utf-8 -*-
import re, json

with open(r'C:\ECNU-个人资料\复习资料\中国当代史\quiz-site\cr_50_new.json', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern: CJK char followed by " followed by non-" text followed by " followed by CJK char/punct
# These are inner quotes that should be Chinese quotation marks
pattern = r'(?<=[一-鿿　-〿＀-￯])"([^"]{1,120}?)"(?=[一-鿿　-〿＀-￯，、。；：])'
new_content = re.sub(pattern, r'“\1”', content)

changes = sum(1 for a, b in zip(content, new_content) if a != b)
print(f'Characters changed: {changes}')

with open(r'C:\ECNU-个人资料\复习资料\中国当代史\quiz-site\cr_50_new.json', 'w', encoding='utf-8') as f:
    f.write(new_content)

# Validate
try:
    data = json.loads(new_content)
    print(f'JSON valid! {len(data)} questions')
except json.JSONDecodeError as e:
    print(f'Still invalid: {e}')
    # Show context
    pos = e.pos
    print(f'Around position {pos}: ...{new_content[pos-30:pos+30]}...')
