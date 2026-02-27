$file = "index (1).html"
$content = [System.IO.File]::ReadAllText($file)

# Replace product section heading
$content = $content -replace 'CloudMeld Hosting is your AI-powered financial copilot', 'Our Hosting Solutions'
Write-Host "OK: Product heading"

# Replace product section description
$content = $content -replace 'Forget about spreadsheets.*?you always know where you stand\.', 'Choose the hosting plan that fits your needs. Our three tiers are designed to scale with your business. From starter websites to enterprise applications, CloudMeld Hosting delivers reliable, fast, and secure infrastructure.'
Write-Host "OK: Product description"

# Replace CTA button text
$content = $content -replace 'Get instant clarity', 'Explore Plans'
Write-Host "OK: Explore Plans CTA"

# Remove redundant cash flow mention from features section
$content = $content -replace 'CloudMeld Hosting provides everything your website needs: managed deployment, SSL certificates, global CDN, 99\.9% uptime SLA, advanced security, performance optimization, and secure infrastructure', 'Everything your website needs: managed deployment, SSL certificates, global CDN, 99.9% uptime SLA, advanced security, performance optimization, and 24/7 support.'
Write-Host "OK: Features section cleaned"

[System.IO.File]::WriteAllText($file, $content)
Write-Host "Final updates completed!"
