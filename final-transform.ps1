# Final comprehensive transformation for CloudMeld Hosting
$file = "index (1).html"
$content = Get-Content $file -Raw -Encoding UTF8

Write-Host "Starting comprehensive transformation..." -ForegroundColor Cyan

# 1. CREATE SINGLE PRICING CARD (Remove switching UI and create single enterprise card)
$oldPricingSection = @'
<div class="vertical-wrapper-center slide-in-from-bottom"><div class="pricing-switch"><div
'@

$newPricingStart = @'
<div class="vertical-wrapper-center slide-in-from-bottom"><div style="display:none;" class="pricing-switch"><div
'@

$content = $content -replace [regex]::Escape($oldPricingSection), $newPricingStart

# 2. ADD RAZORPAY SCRIPT before </body>
$razorpayScript = @'
<script src="https://checkout.razorpay.com/v1/checkout.js"></script>
<script>
function startPayment() {
  var options = {
    "key": "YOUR_RAZORPAY_KEY_HERE", 
    "amount": "826000",
    "currency": "INR",
    "name": "CloudMeld Hosting",
    "description": "Lifetime Enterprise Cloud Hosting",
    "image": "https://via.placeholder.com/150",
    "handler": function (response){
      alert("Payment successful! Payment ID: " + response.razorpay_payment_id);
      window.location.href = "/thank-you.html";
    },
    "prefill": {
      "name": "",
      "email": "",
      "contact": ""
    },
    "theme": {
      "color": "#7bb07f"
    }
  };
  var rzp = new Razorpay(options);
  rzp.open();
}
</script>
</body></html>
'@

$content = $content -replace '</body></html>', $razorpayScript

# 3. Update pricing description text
$content = $content -replace 'Perfect to explore CloudMeld Hosting and forecast your first cash flow\.', 'Get lifetime enterprise hosting with managed deployment, SSL, CDN, monitoring, and 24/7 support.'

# 4. Update sidebar "Buy on Webflow" link
$content = $content -replace '<a data-w-id="53f35bda-4453-cc15-ca25-280c1d997f60" href="https://webflow\.com/templates/html/fundmind-website-template" class="buy-on-webflow-link w-inline-block"><div>Buy this Template</div>', '<a data-w-id="53f35bda-4453-cc15-ca25-280c1d997f60" href="#pricing" onclick="startPayment(); return false;" class="buy-on-webflow-link w-inline-block"><div>Purchase Hosting</div>'

# 5. Update footer email
$content = $content -replace 'hello@clearboard\.fr', 'hello@cloudmeld.hosting'

# 6. Update contact form heading
$content = $content -replace '<h2>Start forecasting your cash flow with CloudMeld Hosting today\.</h2>', '<h2>Get lifetime enterprise hosting for your business.</h2>'

# 7. Update contact section paragraph
$content = $content -replace 'No spreadsheets\. No stress\. Just smarter financial decisions — powered by AI\. Get started in minutes with our free version\.', 'No monthly fees. No surprises. Just reliable, managed hosting with enterprise features at a one-time price of Rs. 8260 (incl. GST).'

# 8. Update Request Demo buttons to Purchase Hosting
$content = $content -replace '>Request a free demo<', '>Purchase Hosting<'
$content = $content -replace '>Get instant clarity<', '>Purchase Hosting<'
$content = $content -replace '>Try your first scenario simulation<', '>View Pricing<'
$content = $content -replace '>Start your free demo now<', '>Purchase Hosting Now<'

# Write back
$content | Set-Content $file -Encoding UTF8 -NoNewline

Write-Host "Transformation completed successfully!" -ForegroundColor Green
Write-Host "- Added Razorpay integration" -ForegroundColor Yellow
Write-Host "- Updated pricing section" -ForegroundColor Yellow
Write-Host "- Updated CTAs to Purchase Hosting" -ForegroundColor Yellow
Write-Host "- Updated contact information" -ForegroundColor Yellow
