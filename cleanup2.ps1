$file = "index (1).html"
$content = [System.IO.File]::ReadAllText($file)

# Remove "AI-powered financial copilot" and replace with hosting focus
$content = $content -replace 'CloudMeld Hosting is your AI-powered financial', 'CloudMeld Hosting is your managed cloud hosting'
$content = $content -replace 'cloudmeld hosting is your ai-powered financial', 'cloudmeld hosting is your managed cloud hosting'

# Replace "smarter decisions" section
$content = $content -replace 'Make.*?smarter decisions.*?faster', 'Website Performance & Reliability Details'
$content = $content -replace 'CloudMeld Hosting lets you simulate real-life business scenarios.*?data-backed decisions in seconds\.', 'CloudMeld Hosting provides comprehensive analytics and monitoring for your hosted websites, ensuring optimal performance and reliability.'

# Replace "Try your first scenario simulation" CTA
$content = $content -replace 'Try your first scenario simulation', 'View Performance Metrics'

# Replace "Made for busy teams" section
$content = $content -replace 'Get set up.*?in minutes.*?no finance degree required', 'Get your website live in minutes with simple setup'
$content = $content -replace 'CloudMeld Hosting was built for founders, COOs, and business owners.*?everything you need is in one place\.', 'CloudMeld Hosting is built for businesses of all sizes. Simple setup, powerful tools, and dedicated support to ensure your website stays online and fast.'

# Replace "Start your free demo now" CTA
$content = $content -replace 'Start your free demo now', 'Get Started Today'

# Replace "Choose the right plan" pricing intro
$content = $content -replace 'Start with a free trial and upgrade when you.*?just powerful financial tools tailored to your needs\.', 'Start with our most affordable plan and upgrade as you grow. No hidden fees, no surprises — just reliable hosting tailored to your business needs.'

# Replace FAQ questions about financial features
$content = $content -replace 'Do I need a finance background to use CloudMeld Hosting\?', 'What level of uptime does CloudMeld Hosting guarantee?'
$content = $content -replace 'The platform is simple, visual, and designed to be used without financial expertise\.', 'CloudMeld Hosting offers a 99.9% uptime SLA backed by our global infrastructure and redundant systems.'

$content = $content -replace 'How long does CloudMeld Hosting setup take\?', 'Can I migrate my existing website to CloudMeld Hosting?'
$content = $content -replace 'Less than 5 minutes\. Just connect your bank account, and CloudMeld Hosting starts generating insights immediately\. No complicated onboarding\.', 'Yes. Our migration specialists can help transfer your website with zero downtime. We handle DNS configuration and all technical details.'

[System.IO.File]::WriteAllText($file, $content)
Write-Host "Additional sections updated!"
