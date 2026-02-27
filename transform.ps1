# Transform ClearBoard to CloudMeld Hosting
$file = "index (1).html"
$content = Get-Content $file -Raw -Encoding UTF8

# Replace brand mentions throughout
$content = $content -replace 'ClearBoard', 'CloudMeld Hosting'

# Replace "from 3K+ reviews" which was partially updated
$content = $content -replace 'from 3K\+ reviews', 'from 500+ businesses'

# Features section description 
$content = $content -replace 'From automated forecasting to real-time insights, CloudMeld Hosting gives you the tools you need to monitor, predict, and improve your company''s cash flow — effortlessly\.', 'CloudMeld Hosting provides fully managed cloud hosting with enterprise-level security, performance, and reliability. Focus on your business while we handle your infrastructure.'

# Write the modified content back
$content | Set-Content $file -Encoding UTF8 -NoNewline

Write-Host "Transformation complete" -ForegroundColor Green
