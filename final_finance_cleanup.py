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

# 1. Features section intro paragraph
if "automated forecasting to real-time insights" in content:
    content = content.replace(
        "From automated forecasting to real-time insights, CloudMeld Hosting gives you the tools you need to monitor, predict, and improve your company's cash flow — effortlessly.",
        "From automated deployments to real-time monitoring, CloudMeld Hosting gives you the tools you need to deploy, manage, and scale your websites — effortlessly."
    )
    print("✓ Replaced: Features section intro paragraph")
    replacements_made += 1

# 2. Feature card description with double dots
if "Predict your company's financial future in seconds.." in content:
    content = content.replace(
        "Predict your company's financial future in seconds..",
        "Deploy your website infrastructure in minutes."
    )
    print("✓ Replaced: Feature card description (with double dots)")
    replacements_made += 1

# 3. Alternative versions in case there are spacing differences
if "automated forecasting" in content:
    # Flexible regex replacement for any version
    pattern = r'From automated forecasting[^<]+?cash flow[^<]+?effortlessly\.'
    replacement = 'From automated deployments to real-time monitoring, CloudMeld Hosting gives you the tools you need to deploy, manage, and scale your websites — effortlessly.'
    content = re.sub(pattern, replacement, content)
    print("✓ Replaced: Features intro (flexible match)")
    replacements_made += 1

if "financial future in seconds" in content:
    pattern = r'Predict your company[\'']?s? financial future[^<]+'
    replacement = 'Deploy your website infrastructure in minutes. '
    content = re.sub(pattern, replacement, content)
    print("✓ Replaced: Financial future reference (flexible match)")
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
