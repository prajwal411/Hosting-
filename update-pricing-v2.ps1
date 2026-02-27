# Comprehensive Pricing Section Update Script
$filePath = "c:\Users\abhis\Documents\Abhishek_Documents\websites\vercelhost\index (1).html"

# Read entire file
$content = Get-Content $filePath -Raw -Encoding UTF8

Write-Host "Original file size: $($content.Length) characters"

# 1. Update pricing section title
$content = $content -replace 'Choose the <span class="text-color-green-700 text-style-italic">right plan</span> for you and your business', 'Simple, <span class="text-color-green-700 text-style-italic">Transparent</span> Pricing'

# 2. Update pricing section subtitle  
$oldSubtitle = 'Start with a free trial and upgrade when you.{1,3}re ready\. No hidden fees, no surprises .{1,3} just powerful financial tools tailored to your needs\.'
$newSubtitle = 'One-time infrastructure setup. No monthly fees. No hidden costs.'
$content = $content -replace $oldSubtitle, $newSubtitle

# 3. Update Starter plan
$content = $content -replace '<div class="heading-style-4 no-margin">Starter</div>', '<div class="heading-style-4 no-margin">Starter Hosting</div>'
$content = $content -replace '<div class="pricing-tag">Free Forever</div>', '<div class="pricing-tag">One-Time</div>'
$content = $content -replace 'Perfect to explore CloudMeld Hosting and forecast your first cash flow\.', 'Perfect for small businesses needing reliable hosting.'

# Update Starter price (looking for "Free" in the price div)
$content = $content -replace '<div class="heading-style-2 no-margin">Free</div>', '<div class="heading-style-2 no-margin">₹8260</div>'
# Update price subtitle from empty space to GST text  
$pattern1 = '<div class="text-size-large text-style-muted"> </div>'
$replacement1 = '<div class="text-size-large text-style-muted">(incl. GST)</div>'
$content = $content -replace [regex]::Escape($pattern1), $replacement1

# 4. Update Pro to Business Hosting
$content = $content -replace '<div class="heading-style-4 no-margin">Pro</div>', '<div class="heading-style-4 no-margin">Business Hosting</div>'
$content = $content -replace '<div class="pricing-tag">Recommended</div>', '<div class="pricing-tag">Most Popular</div>'
$content = $content -replace 'Everything in Free, plus powerful tools to simulate and plan ahead\.', 'For growing brands, service companies, agencies.'
# Update Business price
$content = $content -replace '₹17700', '₹21,240'

# 5. Update Team to Enterprise Hosting
$content = $content -replace '<div class="heading-style-4 no-margin">Team</div>', '<div class="heading-style-4 no-margin">Enterprise Hosting</div>'
$content = $content -replace 'Everything in Pro, plus features built for teams and multi-entity management\.', 'For high-traffic platforms, agencies, SaaS.'
$content = $content -replace '<div class="heading-style-2 no-margin">Custom</div>', '<div class="heading-style-2 no-margin">₹41,300</div>'
$content = $content -replace '<div class="text-size-large text-style-muted">Enterprise</div>', '<div class="text-size-large text-style-muted">(incl. GST)</div>'

# 6. Update Starter features
$content = $content -replace '<div>Features:</div>', '<div>Includes:</div>'
$content = $content -replace '1 connected bank account', '1 Website'
$content = $content -replace '30-day cash flow forecast', 'Domain Setup'
$content = $content -replace 'Expense tracking', 'SSL Certificate'  
$content = $content -replace 'Limited Email support', 'Email Support'

# 7. Update Business features  
$content = $content -replace 'All features in Free, plus :', 'Includes:'
$content = $content -replace 'Up to 3 bank accounts', 'Up to 3 Websites'
$content = $content -replace '90-day forecast', 'Priority Deployment'
$content = $content -replace 'Scenario simulation', 'Performance Optimization'
$content = $content -replace 'Custom tags &amp; insights', 'Advanced Monitoring'

# 8. Update Enterprise features
$content = $content -replace 'All features in Pro, plus :', 'Includes:'
$content = $content -replace 'Unlimited bank accounts', 'Unlimited Websites'
$content = $content -replace 'Team access &amp; permissions', 'Dedicated Infrastructure'
$content = $content -replace 'Multi-currency support', 'Custom Configurations'
$content = $content -replace 'Exportable reports &amp; integrations', 'Performance Tuning'

# 9. Update CTAs
$content = $content -replace 'Get started for free', 'Get Started'
$content = $content -replace 'Upgrade to pro', 'Choose Plan'
$content = $content -replace 'Contact us', 'Talk to Sales'

# 10. Update notification bar 
$content = $content -replace 'Lifetime managed hosting for', 'Starting at'

Write-Host "Updated file size: $($content.Length) characters"

# Save the file
$content | Set-Content $filePath -Encoding UTF8 -NoNewline

Write-Host "SUCCESS: Pricing section updated!"
Write-Host " * Title changed to: Simple, Transparent Pricing"
Write-Host " * Subtitle: One-time infrastructure setup..."
Write-Host " * Starter Hosting: Price 8260"
Write-Host " * Business Hosting: Price 21,240 - Most Popular"
Write-Host " * Enterprise Hosting: Price 41,300"
Write-Host " * All finance features replaced with hosting features"
