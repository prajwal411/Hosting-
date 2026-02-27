#!/usr/bin/env python3
"""Replace remaining CloudMeld Hosting references with vercelhosting"""

file_path = "c:\\Users\\abhis\\Documents\\Abhishek_Documents\\websites\\vercelhost\\index (1).html"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

original_size = len(content)

# Additional replacements for remaining references
additional_replacements = [
    ('Here\'s everything you need to know about CloudMeld Hosting.', 'Here\'s everything you need to know about vercelhosting.'),
    ('"CloudMeld Hosting has completely changed the way we manage our web hosting.', '"vercelhosting has completely changed the way we manage our web hosting.'),
    ('name: \'CloudMeld Hosting\',', 'name: \'vercelhosting\','),
]

count = 0
for old, new in additional_replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1
        print(f"✓ Replaced: {old[:60]}...")

# Save the updated file
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

new_size = len(content)
size_change = new_size - original_size

print(f"\n✅ Remaining references updated!")
print(f"Replacements made: {count}")
print(f"File size change: {size_change:+} characters")
