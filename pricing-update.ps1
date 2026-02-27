$file = "index (1).html"
$content = [System.IO.File]::ReadAllText($file)

# Update pricing plan names and descriptions
$content = $content -replace 'Starter', 'Starter Hosting'
$content = $content -replace 'Pro', 'Business Hosting'
$content = $content -replace 'Team', 'Enterprise Hosting'

# Update Free pricing
$content = $content -replace 'Free Forever', 'One-Time Fee'

# Replace pricing for Starter - Annual version ($29/month pattern with Free)
$content = $content -replace 'Free</div><div class="text-size-large text-style-muted"> </div></div><div class="features-wrapper"><div>Features:</div><div class="advantage"><div class="advantage-icon-wrapper"><img loading="lazy" src="https://wubflow-shield.NOCODEXPORT.DEV/68303fa72b95b93d84bd1241/6830668478aa01087f286888_Check_Light.svg" alt="Check icon" class="advantage-icon" /></div><div>5 GB storage space</div></div><div class="advantage"><div class="advantage-icon-wrapper"><img loading="lazy" src="https://wubflow-shield.NOCODEXPORT.DEV/68303fa72b95b93d84bd1241/6830668478aa01087f286888_Check_Light.svg" alt="Check icon" class="advantage-icon" /></div><div>Global CDN acceleration</div></div><div class="advantage"><div class="advantage-icon-wrapper"><img loading="lazy" src="https://wubflow-shield.NOCODEXPORT.DEV/68303fa72b95b93d84bd1241/6830668478aa01087f286888_Check_Light.svg" alt="Check icon" class="advantage-icon" /></div><div>SSL certificate included', '₹8260</div><div class="text-size-large text-style-muted">(One-Time)</div></div><div class="features-wrapper"><div>Includes:</div><div class="advantage"><div class="advantage-icon-wrapper"><img loading="lazy" src="https://wubflow-shield.NOCODEXPORT.DEV/68303fa72b95b93d84bd1241/6830668478aa01087f286888_Check_Light.svg" alt="Check icon" class="advantage-icon" /></div><div>1 Website</div></div><div class="advantage"><div class="advantage-icon-wrapper"><img loading="lazy" src="https://wubflow-shield.NOCODEXPORT.DEV/68303fa72b95b93d84bd1241/6830668478aa01087f286888_Check_Light.svg" alt="Check icon" class="advantage-icon" /></div><div>SSL Included</div></div><div class="advantage"><div class="advantage-icon-wrapper"><img loading="lazy" src="https://wubflow-shield.NOCODEXPORT.DEV/68303fa72b95b93d84bd1241/6830668478aa01087f286888_Check_Light.svg" alt="Check icon" class="advantage-icon" /></div><div>Basic Monitoring'

# Update Product Section heading
$content = $content -replace 'Built with real-time intelligence', 'Multiple Hosting Plans'

# Update Product Section main heading
$content = $content -replace 'CloudMeld Hosting is your managed cloud hosting <span class="text-color-yellow-700 text-style-italic">copilot</span>', 'Our Hosting <span class="text-color-yellow-700 text-style-italic">Solutions</span>'

# Update CTA from "Get instant clarity" to "Choose Plan"
$content = $content -replace 'Get instant clarity', 'Choose Plan'

# Update Product description
$content = $content -replace 'Choose the hosting plan that fits your needs\. Our three tiers are designed to scale with your business\. From starter websites to enterprise applications, CloudMeld Hosting delivers reliable, fast, and secure infrastructure\.', 'Select the hosting plan that fits your needs. All plans include 24/7 support, automatic backups, and enterprise-grade security.'

Write-Host "Pricing and product section updated!"
[System.IO.File]::WriteAllText($file, $content)
