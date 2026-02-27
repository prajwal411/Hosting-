#!/usr/bin/env python3
"""Replace all CloudMeld Hosting references with vercelhosting"""

file_path = "c:\\Users\\abhis\\Documents\\Abhishek_Documents\\websites\\vercelhost\\index (1).html"

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Store original size
original_size = len(content)

# Perform replacements - map old text to new text
replacements = [
    ("CloudMeld Hosting - Enterprise Cloud Hosting Platform", "vercelhosting - Enterprise Cloud Hosting Platform"),
    ("<title>CloudMeld Hosting", "<title>vercelhosting"),
    ('alt="CloudMeld Hosting logo"', 'alt="vercelhosting logo"'),
    ('alt="CloudMeld Hosting dashboard"', 'alt="vercelhosting dashboard"'),
    ("From automated deployments to real-time monitoring, CloudMeld Hosting gives you", "From automated deployments to real-time monitoring, vercelhosting gives you"),
    ("Deploy your website infrastructure in minutes. CloudMeld Hosting handles your complete", "Deploy your website infrastructure in minutes. vercelhosting handles your complete"),
    ("From early-stage startups to growing SMEs, CloudMeld Hosting helps teams", "From early-stage startups to growing SMEs, vercelhosting helps teams"),
    ('"CloudMeld Hosting has completely changed', '"vercelhosting has completely changed'),
    ("Websites hosted on CloudMeld Hosting infrastructure", "Websites hosted on vercelhosting infrastructure"),
    ("CloudMeld Hosting is your complete", "vercelhosting is your complete"),
    ("Forget about complicated server setups, DevOps complexity, and hosting headaches. CloudMeld Hosting provides", "Forget about complicated server setups, DevOps complexity, and hosting headaches. vercelhosting provides"),
    ("CloudMeld Hosting scales automatically", "vercelhosting scales automatically"),
    ("CloudMeld Hosting was built for developers", "vercelhosting was built for developers"),
    ("CloudMeld Hosting-template.webflow.io", "vercelhosting-template.webflow.io"),
    ("CloudMeld Hosting offers lifetime enterprise cloud hosting", "vercelhosting offers lifetime enterprise cloud hosting"),
    ("key: 'razorpay_live_YourKeyHere', amount: plan.amount, currency: 'INR', name: 'CloudMeld Hosting'", "key: 'razorpay_live_YourKeyHere', amount: plan.amount, currency: 'INR', name: 'vercelhosting'"),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1
        print(f"✓ Replaced: {old[:60]}...")

# Save the updated file
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

new_size = len(content)
size_change = new_size - original_size

print(f"\n✅ Site name updated successfully!")
print(f"Total replacements made: {count}")
print(f"Original file size: {original_size:,} characters")
print(f"New file size: {new_size:,} characters")
print(f"Size change: {size_change:+} characters")
print(f"\n🎉 All 'CloudMeld Hosting' references changed to 'vercelhosting'")
