import re

# File path
file_path = r"c:\Users\abhis\Documents\Abhishek_Documents\websites\vercelhost\index (1).html"

# Read file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original file size: {len(content)} characters")
print("=" * 60)

# Additional replacements for remaining finance references
remaining_replacements = [
    # Features section intro
    ("From automated forecasting to real-time insights, CloudMeld Hosting gives you the tools you need to monitor, predict, and improve your company's cash flow — effortlessly.", 
     "From automated deployments to real-time monitoring, CloudMeld Hosting gives you the tools you need to deploy, manage, and scale your websites — effortlessly."),
    
    # Features card description - the one with double dots
    ("Predict your company's financial future in seconds..", 
     "Deploy your website infrastructure in minutes."),
    
    # Testimonials section intro
    ("CloudMeld Hosting helps teams make confident financial decisions — without relying on outdated spreadsheets or guesswork.",
     "CloudMeld Hosting helps teams deploy and manage their websites confidently — without wrestling with complex server configurations or DevOps challenges."),
]

replacement_count = 0
for old, new in remaining_replacements:
    if old in content:
        content = content.replace(old, new)
        replacement_count += 1
        print(f"✓ Replaced: '{old[:60]}...'")

print("=" * 60)
print(f"Total replacements made: {replacement_count}/{len(remaining_replacements)}")

# Check for remaining finance terms
finance_terms = ['bank account', 'bank data', 'finance background', 'financial', 'cash flow', 'spreadsheet', 'forecast']
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
