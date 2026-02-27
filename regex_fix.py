import re

# File path
file_path = r"c:\Users\abhis\Documents\Abhishek_Documents\websites\vercelhost\index (1).html"

# Read file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original file size: {len(content)} characters")
print("=" * 60)

# Use regex to match any apostrophe-like character
pattern = r"Predict your company.s financial future in seconds\.\."
replacement = "Deploy your website infrastructure in minutes."

if re.search(pattern, content):
    content = re.sub(pattern, replacement, content)
    print("+ Replaced: Feature card description (regex match)")
    replacements_made = 1
else:
    print("- Pattern not found")
    replacements_made = 0

print("=" * 60)
print(f"Total replacements made: {replacements_made}")

# Check for remaining finance terms
finance_terms = ['financial', 'cash flow', 'forecast']
remaining = {}

for term in finance_terms:
    count = len(re.findall(term, content, re.IGNORECASE))
    if count > 0:
        remaining[term] = count

print("=" * 60)
if remaining:
    print("WARNING: Remaining finance references:")
    for term, count in remaining.items():
        print(f"  - {term}: {count}")
else:
    print("SUCCESS! ALL FINANCE REFERENCES REMOVED!")
    print("Your CloudMeld Hosting website is 100% hosting-focused!")

print(f"\nUpdated file size: {len(content)} characters")

# Write file
with open(file_path, 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print("=" * 60)
print("+ File saved successfully!")
