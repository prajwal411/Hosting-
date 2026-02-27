$file = "index (1).html"
$content = [System.IO.File]::ReadAllText($file)

# Simple text replacements without special characters
$replacements = @{
    "Automated Cash Flow" = "Managed Deployment & Setup"
    "Get your first forecast now" = "Learn about deployment"
    "Request a free demo" = "Get started now"
    "Smart features" = "Hosting features"
}

foreach ($old in $replacements.Keys) {
    $new = $replacements[$old]
    $content = $content -replace [regex]::Escape($old), $new
}

[System.IO.File]::WriteAllText($file, $content)
Write-Host "Basic replacements completed!"
