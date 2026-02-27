$file = "index (1).html"
$content = [System.IO.File]::ReadAllText($file)

# Remove the forecasting intro part
$content = $content -replace 'From automated forecasting to real-time insights, CloudMeld Hosting gives you the tools you need to monitor, predict, and improve your company.*?cash flow .', ''

# Update the feature card description
$content = $content -replace 'Predict your company.*?spreadsheet required\.', 'Deploy and manage your website with our comprehensive managed hosting solution. Includes DNS configuration, server optimization, SSL setup, and ongoing technical support.'

# Update other finance feature descriptions if present
$content = $content -replace 'Identify areas where you can cut costs and boost revenue\.', 'Secure all your data with enterprise-grade encryption and DDoS protection.'

$content = $content -replace 'Unlock insights about your spending patterns so you can make smarter decisions\.', 'Global content delivery network ensures fast loading times worldwide.'

[System.IO.File]::WriteAllText($file, $content)
Write-Host "Remaining finance content cleaned!"
