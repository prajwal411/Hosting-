$file = "index (1).html"
$content = [System.IO.File]::ReadAllText($file)

# Update numbers grid statistics
$content = $content -replace '<div class="number">92%</div>', '<div class="number">99.9%</div>'
$content = $content -replace '<div class="number">12 hours</div>', '<div class="number">24/7</div>'
$content = $content -replace '<div class="number">100%</div>', '<div class="number">500+</div>'
$content = $content -replace '2300\+', '500+'

# Update the descriptions for the numbers
$content = $content -replace 'Improved uptime and faster deployment within the first week\.', 'Guaranteed uptime SLA backed by our infrastructure.'
$content = $content -replace 'Support availability for critical issues\.', 'Round-the-clock support for your website needs.'
$content = $content -replace 'Availability and redundancy in global infrastructure\.', 'Websites hosted with CloudMeld Hosting globally.'

[System.IO.File]::WriteAllText($file, $content)
Write-Host "Numbers grid updated!"
