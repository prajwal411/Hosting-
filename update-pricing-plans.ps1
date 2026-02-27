$file = "index (1).html"
$content = [System.IO.File]::ReadAllText($file)

# Plan name updates
$content = $content -replace '>Starter<', '>Starter Hosting<'
$content = $content -replace '>Pro<', '>Business Hosting<'  
$content = $content -replace '>Team<', '>Enterprise Hosting<'

# Update Pricing Tags
$content = $content -replace 'Free Forever', 'One-Time'
$content = $content -replace "Let's scale", 'Custom'

# Update plan descriptions
$content = $content -replace 'Everything in Free, plus powerful tools to simulate and plan ahead\.', 'For growing brands and service companies.'
$content = $content -replace 'Everything in Pro, plus features built for teams and multi-entity management\.', 'For agencies and high-traffic platforms.'

# Update CTA buttons  
$content = $content -replace 'Get started for free', 'Get Started'
$content = $content -replace 'Upgrade to pro', 'Choose Plan'
$content = $content -replace 'Contact us', 'Talk to Sales'

# Update pricing intro text
$content = $content -replace 'Start with our most affordable plan and upgrade as you grow.', 'One-time infrastructure setup fee. Includes lifetime managed hosting.'

# Update feature labels
$content = $content -replace 'All features in Free, plus :', 'Includes:'
$content = $content -replace 'All features in Pro, plus :', 'Includes:'

Write-Host "Pricing plans updated successfully!"
[System.IO.File]::WriteAllText($file, $content)
