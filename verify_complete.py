import re

file_path = r"c:\Users\abhis\Documents\Abhishek_Documents\websites\vercelhost\index (1).html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print("=" * 70)
print("CLOUDMELD HOSTING - TRANSFORMATION COMPLETE!")
print("=" * 70)

# Section counts
sections = {
    'Pricing': content.count('id="pricing"'),
    'FAQ': content.count('id="faqs"'),
    'Features': content.count('id="features"'),
    'Testimonials': content.count('id="testimonials"'),
    'Product': content.count('id="product"'),
    'Contact': content.count('id="contact"')
}

print("\nSection Structure:")
for name, count in sections.items():
    status = "OK" if count == 1 else "ERROR"
    print(f"  {name:15} {count} section(s)  [{status}]")

# Finance terms check
finance_terms = ['financial', 'cash flow', 'forecast', 'spreadsheet', 'bank account', 'bank data']
print("\nFinance Content Check:")
total_finance = 0
for term in finance_terms:
    count = len(re.findall(term, content, re.IGNORECASE))
    total_finance += count
    print(f"  {term:15} {count} occurrence(s)")

print(f"\n  TOTAL: {total_finance} finance references")

# Hosting terms verification
hosting_terms = ['hosting', 'deployment', 'SSL', 'CDN', 'uptime', 'infrastructure']
print("\nHosting Content Check:")
total_hosting = 0
for term in hosting_terms:
    count = len(re.findall(term, content, re.IGNORECASE))
    total_hosting += count
    print(f"  {term:15} {count} occurrence(s)")

# Pricing check
prices = ['8260', '21,240', '41,300']
print("\nPricing Verification:")
for price in prices:
    count = content.count(price)
    print(f"  Rs {price:8} {count} occurrence(s)")

# File statistics
print("\nFile Statistics:")
print(f"  Total size: {len(content):,} characters")
print(f"  Original:   138,765 characters")
print(f"  Reduced by: {138765 - len(content):,} characters")

# Overall status
print("\n" + "=" * 70)
if total_finance == 0 and all(count == 1 for count in sections.values()):
    print("STATUS: SUCCESS - Website is 100% hosting-focused!")
    print("All finance content removed, all sections clean!")
else:
    print("STATUS: NEEDS ATTENTION")
    if total_finance > 0:
        print(f"  - {total_finance} finance references still present")
    if not all(count == 1 for count in sections.values()):
        print("  - Section count issues detected")
print("=" * 70)
