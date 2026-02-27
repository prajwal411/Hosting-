import re

# File path
file_path = r"c:\Users\abhis\Documents\Abhishek_Documents\websites\vercelhost\index (1).html"

# Read file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original file size: {len(content)} characters")
print("=" * 60)

# Finance to Hosting replacements
replacements = [
    # Features section
    ("monitor, predict, and improve your company's cash flow", "deploy, manage, and scale your websites"),
    ("Automated Cash Flow", "Automated Deployment"),
    ("Predict your company's financial future in seconds", "Deploy your website infrastructure in minutes"),
    ("CloudMeld Hosting analyzes your bank transactions and generates 30-, 60-, and Priority Deployments", "CloudMeld Hosting handles your complete deployment pipeline with automated SSL, CDN setup, and continuous monitoring"),
    ("updated daily, no spreadsheet required", "updated automatically, no server management required"),
    ("Get your first forecast now", "Start hosting now"),
    
    # Testimonials
    ("manage our finances", "manage our web hosting"),
    ("We went from reactive to proactive in just a few days", "We went from manual setup to automated deployment in just minutes"),
    ("The cash flow forecasting is insanely accurate", "The deployment process is incredibly smooth"),
    ("scenario feature helped us plan a key hire with confidence", "hosting infrastructure scaled beautifully with our growth"),
    
    # Stats section
    ("Better visibility on their cash flow within the first week", "Websites deployed and live within the first hour"),
    ("Saved per month on manual financial reporting", "Saved per month on server management and DevOps"),
    ("Bank-level data encryption and privacy compliance", "Enterprise-grade SSL encryption and security"),
    ("Businesses use CloudMeld Hosting to manage their finances", "Websites hosted on CloudMeld Hosting infrastructure"),
    
    # Product/Features sections
    ("Forget about spreadsheets, formulas, and financial guesswork", "Forget about complicated server setups, DevOps complexity, and hosting headaches"),
    ("CloudMeld Hosting connects securely to your bank accounts, understands your cash flow patterns, and delivers real-time insights that actually help you run your business", "CloudMeld Hosting provides enterprise-grade infrastructure with automated deployments, SSL certificates, global CDN, and 24/7 monitoring that keeps your websites running smoothly"),
    ("Whether you're managing growth or bracing for uncertainty, you always know where you stand", "whether you're launching your first site or scaling to millions of users, your hosting infrastructure is ready"),
    ("Get instant clarity", "Get Started Now"),
    
    # Scenario/Planning section
    ("Make <span class=\"text-color-yellow-700 text-style-italic\">smarter decisions</span>, faster", "Scale <span class=\"text-color-yellow-700 text-style-italic\">effortlessly</span>, globally"),
    ("CloudMeld Hosting lets you simulate real-life business scenarios — from hiring a new team member to investing in equipment or navigating a cash crunch. See the financial impact of your choices before you make them. No more blind spots. Just confident, data-backed decisions in seconds", "CloudMeld Hosting scales automatically with your traffic — from a few visitors to thousands of concurrent users. Handle traffic spikes, deploy globally with CDN, and monitor performance in real-time. No server crashes. Just reliable, fast hosting infrastructure that grows with you"),
    ("Try your first scenario simulation", "View Hosting Plans"),
    
    # Finance setup section
    ("no finance degree required", "no DevOps experience required"),
    ("CloudMeld Hosting was built for founders, COOs, and business owners — not just financial experts", "CloudMeld Hosting was built for developers, agencies, and businesses — not just system administrators"),
    ("With an intuitive interface, no jargon, and a guided onboarding, you'll be making smarter financial calls from day one", "With automated setup, zero configuration required, and managed infrastructure, your websites will be live from day one"),
    ("No need to chase your accountant or wait for reports — everything you need is in one place", "No need to manage servers or configure infrastructure — everything is handled automatically"),
    ("Start your free demo now", "Get Started Today"),
    
    # Additional hosting-specific updates ("Made for busy teams" section already says financial experts, etc)
    ("financial experts", "infrastructure experts"),
    ("financial calls", "deployment decisions"),
]

replacement_count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        replacement_count += 1
        print(f"✓ Replaced: '{old[:50]}...' → '{new[:50]}...'")

print("=" * 60)
print(f"Total replacements made: {replacement_count}/{len(replacements)}")

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
    print("✓ All major finance references removed!")

print(f"Updated file size: {len(content)} characters")

# Write file
with open(file_path, 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print("=" * 60)
print("✓ SUCCESS: Content transformed from finance to hosting!")
