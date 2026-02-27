$file = "index (1).html"
$content = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)

# Update Features Section Description
$content = $content -replace "From automated forecasting to real-time insights, CloudMeld Hosting gives you the tools you need to monitor, predict, and improve your company.s cash flow — effortlessly\.", "CloudMeld Hosting provides everything your website needs: managed deployment, SSL certificates, global CDN, 99.9% uptime SLA, advanced security, performance optimization, and 24/7 support."

# Update First Feature Card
$content = $content -replace "<h3 class=""heading-style-4"">Automated Cash Flow</h3>", "<h3 class=""heading-style-4"">Managed Deployment & Setup</h3>"
$content = $content -replace "Predict your company.s financial future in seconds\.\. CloudMeld Hosting analyzes your bank transactions and generates 30-, 60-, and 90-day forecasts — updated daily, no spreadsheet required\.", "We handle full production deployment, DNS configuration, server optimization, and ongoing support setup. No technical knowledge required."
$content = $content -replace "<div>Get your first forecast now</div>", "<div>Learn about deployment</div>"

# Update Testimonials Section
$content = $content -replace "<span class=""text-color-pink-700 text-style-italic"">Trusted</span> by modern businesses to manage what matters most\.", "<span class=""text-color-pink-700 text-style-italic"">Trusted</span> by modern businesses for reliable hosting."
$content = $content -replace "From early-stage startups to growing SMEs, CloudMeld Hosting helps teams make confident financial decisions — without relying on outdated spreadsheets or guesswork\.", "From early-stage startups to growing SMEs, CloudMeld Hosting helps teams run reliable, secure websites on managed enterprise infrastructure."

# Update Testimonial Quote
$content = $content -replace ""CloudMeld Hosting has completely changed the way we manage our finances\. We went from reactive to proactive in just a few days\. The cash flow forecasting is insanely accurate, and the scenario feature helped us plan a key hire with confidence\."", ""CloudMeld Hosting transformed our website performance and reliability. The managed deployment process was seamless, and we've had zero downtime since we launched. Highly recommended for any growing business.""

# Update Product Section Heading
$content = $content -replace "CloudMeld Hosting is your AI-powered financial <span class=""text-color-yellow-700 text-style-italic"">copilot</span>", "Our Hosting <span class=""text-color-yellow-700 text-style-italic"">Solutions</span>"

# Update Product Section Content
$content = $content -replace "Forget about spreadsheets, formulas, and financial guesswork\. CloudMeld Hosting connects securely to your bank accounts, understands your cash flow patterns, and delivers real-time insights that actually help you run your business\.Whether you.re managing growth or bracing for uncertainty, you always know where you stand\.", "Managed hosting infrastructure designed for modern businesses. Automatic deployment, SSL certificates, CDN acceleration, 99.9% uptime guarantee, advanced security, performance optimization, and dedicated 24/7 monitoring included."

# Write back the file
[System.IO.File]::WriteAllText($file, $content, [System.Text.Encoding]::UTF8)
Write-Host "Hosting transformation completed successfully!"
