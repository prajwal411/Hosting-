import re

# File path
file_path = r"c:\Users\abhis\Documents\Abhishek_Documents\websites\vercelhost\index (1).html"

# Read file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original file size: {len(content)} characters")
print("=" * 60)

# Final precision replacements
replacements_made = 0

# 1. Feature card description with double dots
if "Predict your company's financial future in seconds" in content:
    content = content.replace(
        "Predict your company's financial future in seconds..",
        "Deploy your website infrastructure in minutes."
    )
    print("✓ Replaced: Feature card description (with double dots)")
    replacements_made += 1

# 2. Alternative single dot version
if "Predict your company's financial future in seconds." in content and replacements_made == 0:
    content = content.replace(
        "Predict your company's financial future in seconds.",
        "Deploy your website infrastructure in minutes."
    )
    print("✓ Replaced: Feature card description (single dot)")
    replacements_made += 1

# 3. Features section intro - flexible regex
if "cast flow" in content or "automated forecasting" in content:
    pattern = r'From automated forecasting[^<]+?effortlessly\.'
    replacement = 'From automated deployments to real-time monitoring, CloudMeld Hosting gives you the tools you need to deploy, manage, and scale your websites — effortlessly.'
    before_len = len(content)
    content = re.sub(pattern, replacement, content)
    if len(content) != before_len:
        print("✓ Replaced: Features intro paragraph")
        replacements_made += 1

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
    print("⚠ Remaining finance references:")
    for term, count in remaining.items():
        print(f"  - {term}: {count}")
else:
    print("✓✓✓ ALL FINANCE REFERENCES REMOVED! ✓✓✓")

print(f"Updated file size: {len(content)} characters")

# Write file
with open(file_path, 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print("=" * 60)
print("✓ File updated successfully!")
