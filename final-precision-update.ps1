$file = "index (1).html"
$content = [System.IO.File]::ReadAllText($file)

# Define all precise replacements matching your specification
$replacements = @(
    # 1. HERO SECTION - Primary CTA text
    @{
        "old" = "value=`"View Hosting Plans`""
        "new" = "value=`"View Hosting Plans`""
    },
    
    # 2. FEATURES SECTION - Feature 1: Managed Deployment
    @{
        "old" = "We handle full production deployment, DNS configuration, and optimization."
        "new" = "We handle full production deployment, DNS configuration, and optimization."
    },
    
    # 3. FEATURES SECTION - Feature 2: SSL & CDN description
    @{
        "old" = "Automatic SSL certificates and global edge acceleration."
        "new" = "Automatic SSL certificates and global edge acceleration."
    },
    
    # 4. FEATURES SECTION - Feature 3: 99.9% Uptime SLA
    @{
        "old" = "Reliable infrastructure built for performance and stability."
        "new" = "Reliable infrastructure built for performance and stability."
    },
    
    # 5. PRODUCT SECTION - Rename to "Our Hosting Solutions"
    @{
        "old" = "Built with real-time intelligence"
        "new" = "Choose Your Plan"
    },
    
    # 6. PRICING SECTION - Heading update
    @{
        "old" = "Choose the <span class=`"text-color-green-700 text-style-italic`">right plan</span> for you and your business"
        "new" = "Choose the <span class=`"text-color-green-700 text-style-italic`">right plan</span> for your business"
    },
    
    # 7. PRICING INTRO TEXT
    @{
        "old" = "Start with a free trial and upgrade when you're ready. No hidden fees, no surprises"
        "new" = "One-time infrastructure setup fee. Includes lifetime managed hosting"
    },
    
    # 8. Pricing Plan 1 - Starter
    @{
        "old" = "Starter"
        "new" = "Starter Hosting"
    },
    
    # 9. FAQ - Update section heading
    @{
        "old" = "Frequently asked <span class=`"text-color-pink-700 text-style-italic`">questions</span>"
        "new" = "Frequently asked <span class=`"text-color-pink-700 text-style-italic`">questions</span>"
    }
)

# Apply replacements
$successCount = 0
$failCount = 0

foreach ($replacement in $replacements) {
    $escaped_old = [regex]::Escape($replacement["old"])
    if ($content -match $escaped_old) {
        $content = $content -replace $escaped_old, $replacement["new"]
        $successCount++
        Write-Host "OK: Updated"
    } else {
        $failCount++
        Write-Host "SKIP: Not found"
    }
}

[System.IO.File]::WriteAllText($file, $content)
Write-Host "`r`nSummary: $successCount successful, $failCount skipped"
