import re

# File path
file_path = r"c:\Users\abhis\Documents\Abhishek_Documents\websites\vercelhost\index (1).html"

# Read file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original file size: {len(content)} characters")

# Find and replace the finance content with hosting content
# Old: "CloudMeld Hosting is your AI-powered financial copilot"
# New: "CloudMeld Hosting is your enterprise hosting solution"

content = content.replace(
    'CloudMeld Hosting is your AI-powered financial <span class="text-color-yellow-700 text-style-italic">copilot</span>',
    'CloudMeld Hosting is your complete <span class="text-color-yellow-700 text-style-italic">hosting</span> solution'
)

# Old: "Forget about spreadsheets, formulas, and financial guesswork. CloudMeld Hosting connects securely to your bank accounts, understands your cash flow patterns, and delivers real-time insights that actually help you run your business.Whether you're managing growth or bracing for uncertainty, you always know where you stand."
# New: Hosting-focused content

old_paragraph = "Forget about spreadsheets, formulas, and financial guesswork. CloudMeld Hosting connects securely to your bank accounts, understands your cash flow patterns, and delivers real-time insights that actually help you run your business.Whether you're managing growth or bracing for uncertainty, you always know where you stand."

new_paragraph = "Forget about complicated hosting setups, server management, and technical headaches. CloudMeld Hosting provides enterprise-grade infrastructure with managed deployment, automatic SSL certificates, global CDN, and 24/7 monitoring. Whether you're launching your first website or scaling to thousands of users, your hosting is handled."

content = content.replace(old_paragraph, new_paragraph)

print(f"Updated file size: {len(content)} characters")

# Check for any remaining finance references
finance_terms = ['bank account', 'bank data', 'finance background', 'financial', 'cash flow', 'spreadsheet']
remaining_refs = []

for term in finance_terms:
    if term.lower() in content.lower():
        count = content.lower().count(term.lower())
        remaining_refs.append(f"{term}: {count}")

if remaining_refs:
    print(f"⚠ Remaining finance references: {', '.join(remaining_refs)}")
else:
    print("✓ No finance references found!")

# Write file
with open(file_path, 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print("✓ SUCCESS: Finance content replaced with hosting content!")
