$file = "index (1).html"
$content = [System.IO.File]::ReadAllText($file)

# Update pricing plan features
$content = $content -replace 'Up to 3 bank accounts', 'Up to 3 websites'
$content = $content -replace 'Unlimited bank accounts', 'Unlimited websites'
$content = $content -replace '90-day forecast', '100 GB storage'
$content = $content -replace 'Scenario simulation', '5 email accounts'
$content = $content -replace 'Multi-currency support', 'Priority support'
$content = $content -replace 'Custom tags & insights', 'Advanced analytics'
$content = $content -replace 'Exportable reports & integrations', 'API access'

# Update pricing plan descriptions
$content = $content -replace 'Perfect to explore CloudMeld Hosting and start forecasting\.', 'Perfect for small websites and growing businesses.'
$content = $content -replace 'Includes tools to simulate and plan ahead\.', 'With all the features you need for a professional website.'
$content = $content -replace 'Manage advanced forecasts and multi-entity management\.', 'Complete control with advanced features and priority support.'

[System.IO.File]::WriteAllText($file, $content)
Write-Host "Pricing plans updated!"
