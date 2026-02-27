$file = "index (1).html"
$content = [System.IO.File]::ReadAllText($file)

# Define all replacements needed
$replacements = @(
    @{
        "old" = "From automated forecasting to real-time insights, CloudMeld Hosting gives you the tools you need to monitor, predict, and improve your company's cash flow"
        "new" = "CloudMeld Hosting provides everything your website needs: managed deployment, SSL certificates, global CDN, 99.9% uptime SLA, advanced security, performance optimization, and secure infrastructure"
    },
    @{
        "old" = "CloudMeld Hosting has completely changed the way we manage our finances. We went from reactive to proactive in just a few days. The cash flow forecasting is insanely accurate, and the scenario feature helped us plan a key hire with confidence."
        "new" = "CloudMeld Hosting transformed our website performance and reliability. The managed deployment process was seamless, and our uptime improved immediately. Their 24/7 support team is incredibly responsive and helpful."
    },
    @{
        "old" = "CEO at Nexora"
        "new" = "CTO at TechCorp Solutions"
    },
    @{
        "old" = "Better visibility on their cash flow within the first week."
        "new" = "Improved uptime and faster deployment within the first week."
    },
    @{
        "old" = "Saved per month on manual financial reporting."
        "new" = "Support availability for critical issues."
    },
    @{
        "old" = "Bank-level data encryption and privacy compliance."
        "new" = "Availability and redundancy in global infrastructure."
    },
    @{
        "old" = "Businesses use CloudMeld Hosting to manage their finances"
        "new" = "Businesses trust CloudMeld Hosting with their websites"
    },
    @{
        "old" = "Perfect to explore CloudMeld Hosting and forecast your first cash flow."
        "new" = "Perfect for small websites and hobby projects. Start your hosting journey today."
    },
    @{
        "old" = "1 connected bank account"
        "new" = "5 GB storage space"
    },
    @{
        "old" = "30-day cash flow forecast"
        "new" = "Global CDN acceleration"
    },
    @{
        "old" = "Expense tracking"
        "new" = "SSL certificate included"
    }
)

# Apply all replacements
foreach ($replacement in $replacements) {
    $escaped_old = [regex]::Escape($replacement["old"])
    if ($content -match $escaped_old) {
        $content = $content -replace $escaped_old, $replacement["new"]
        $preview = $replacement["old"]
        if ($preview.Length -gt 50) { $preview = $preview.Substring(0, 50) + "..." }
        Write-Host "OK: $preview"
    } else {
        $preview = $replacement["old"]
        if ($preview.Length -gt 50) { $preview = $preview.Substring(0, 50) + "..." }
        Write-Host "SKIP: $preview"
    }
}

[System.IO.File]::WriteAllText($file, $content)
Write-Host "Transformation completed!"
