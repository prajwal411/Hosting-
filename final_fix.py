import re

# File path
file_path = r"c:\Users\abhis\Documents\Abhishek_Documents\websites\vercelhost\index (1).html"

# Read file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original file size: {len(content)} characters")
print("=" * 60)

# The exact text to replace (from the grep output)
old_text = "Predict your company's financial future in seconds.. CloudMeld Hosting handles your complete deployment pipeline with automated SSL, CDN setup, and continuous monitoring"
new_text = "Deploy your website infrastructure in minutes. CloudMeld Hosting handles your complete deployment pipeline with automated SSL, CDN setup, and continuous monitoring"

if old_text in content:
    content = content.replace(old_text, new_text)
    print("+ Replaced: Feature card description with 'financial future'")
    replacements_made = 1
else:
    print("- Exact text not found, trying variations...")
    replacements_made = 0
    
    # Try without the continuation
    old_text_short = "Predict your company's financial future in seconds.."
    new_text_short = "Deploy your website infrastructure in minutes."
    
    if old_text_short in content:
        content = content.replace(old_text_short, new_text_short)
        print("+ Replaced: Short version of feature description")
        replacements_made = 1

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
    print("\nSearching for exact locations...")
    # Show where the terms are
    for term in finance_terms:
        matches = list(re.finditer(term, content, re.IGNORECASE))
        if matches:
            for i, match in enumerate(matches[:3], 1):  # Show first 3 matches
                start = max(0, match.start() - 40)
                end = min(len(content), match.end() + 40)
                context = content[start:end].replace('\n', ' ')
                print(f"\n  Match {i} - '{term}' at position {match.start()}:")
                print(f"    ...{context}...")
else:
    print("SUCCESS! ALL FINANCE REFERENCES REMOVED!")
    print("Your CloudMeld Hosting website is now 100% hosting-focused!")

print(f"\nUpdated file size: {len(content)} characters")

# Write file
with open(file_path, 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print("=" * 60)
print("+ File updated successfully!")
