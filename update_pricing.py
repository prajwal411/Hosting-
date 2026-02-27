import re

# File path
file_path = r"c:\Users\abhis\Documents\Abhishek_Documents\websites\vercelhost\index (1).html"

# Read file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original file size: {len(content)} characters")

# 1. Update pricing section title
content = re.sub(
    r'Choose the <span class="text-color-green-700 text-style-italic">right plan</span> for you and your business',
    'Simple, <span class="text-color-green-700 text-style-italic">Transparent</span> Pricing',
    content
)

# 2. Update pricing section subtitle
content = re.sub(
   r'Start with a free trial and upgrade when you.{1,3}re ready\. No hidden fees, no surprises .{1,3} just powerful financial tools tailored to your needs\.',
    'One-time infrastructure setup. No monthly fees. No hidden costs.',
    content
)

# 3. Update Starter plan
content = content.replace('<div class="heading-style-4 no-margin">Starter</div>', '<div class="heading-style-4 no-margin">Starter Hosting</div>')
content = content.replace('<div class="pricing-tag">Free Forever</div>', '<div class="pricing-tag">One-Time</div>')
content = content.replace('Perfect to explore CloudMeld Hosting and forecast your first cash flow.', 'Perfect for small businesses needing reliable hosting.')
content = content.replace('<div class="heading-style-2 no-margin">Free</div>', '<div class="heading-style-2 no-margin">₹8260</div>')
content = content.replace('<div class="text-size-large text-style-muted"> </div>', '<div class="text-size-large text-style-muted">(incl. GST)</div>')

# 4. Update Pro to Business Hosting
content = content.replace('<div class="heading-style-4 no-margin">Pro</div>', '<div class="heading-style-4 no-margin">Business Hosting</div>')
content = content.replace('<div class="pricing-tag">Recommended</div>', '<div class="pricing-tag">Most Popular</div>')
content = content.replace('Everything in Free, plus powerful tools to simulate and plan ahead.', 'For growing brands, service companies, agencies.')
content = content.replace('₹17700', '₹21,240')

# 5. Update Team to Enterprise Hosting
content = content.replace('<div class="heading-style-4 no-margin">Team</div>', '<div class="heading-style-4 no-margin">Enterprise Hosting</div>')
content = content.replace('Everything in Pro, plus features built for teams and multi-entity management.', 'For high-traffic platforms, agencies, SaaS.')
content = content.replace('<div class="heading-style-2 no-margin">Custom</div>', '<div class="heading-style-2 no-margin">₹41,300</div>')
content = content.replace('<div class="text-size-large text-style-muted">Enterprise</div>', '<div class="text-size-large text-style-muted">(incl. GST)</div>')

# 6. Update Starter features
content = content.replace('<div>Features:</div>', '<div>Includes:</div>', 1)  # Only first occurrence
content = content.replace('1 connected bank account', '1 Website')
content = content.replace('30-day cash flow forecast', 'Domain Setup')
content = content.replace('Expense tracking', 'SSL Certificate')
content = content.replace('Limited Email support', 'Email Support')

# 7. Update Business features
content = content.replace('All features in Free, plus :', 'Includes:')
content = content.replace('Up to 3 bank accounts', 'Up to 3 Websites')
content = content.replace('90-day forecast', 'Priority Deployment')
content = content.replace('Scenario simulation', 'Performance Optimization')
content = content.replace('Custom tags &amp; insights', 'Advanced Monitoring')

# 8. Update Enterprise features
content = content.replace('All features in Pro, plus :', 'Includes:')
content = content.replace('Unlimited bank accounts', 'Unlimited Websites')
content = content.replace('Team access &amp; permissions', 'Dedicated Infrastructure')
content = content.replace('Multi-currency support', 'Custom Configurations')
content = content.replace('Exportable reports &amp; integrations', 'Performance Tuning')

# 9. Update CTAs
content = content.replace('Get started for free', 'Get Started')
content = content.replace('Upgrade to pro', 'Choose Plan')
content = content.replace('Contact us', 'Talk to Sales')

# 10. Update notification bar
content = content.replace('Lifetime managed hosting for', 'Starting at')

print(f"Updated file size: {len(content)} characters")

# Write file
with open(file_path, 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print("✓ SUCCESS: Pricing section updated!")
print("✓ Title: Simple, Transparent Pricing")
print("✓ Subtitle: One-time infrastructure setup...")
print("✓ Starter Hosting: ₹8260 (incl. GST)")
print("✓ Business Hosting: ₹21,240 (incl. GST) - Most Popular")
print("✓ Enterprise Hosting: ₹41,300 (incl. GST)")
print("✓ All CTA buttons updated")
print("✓ Notification bar updated")
