$file = "index (1).html"
$content = [System.IO.File]::ReadAllText($file)

# Replace "What banks and currencies" FAQ
$content = $content -replace 'What banks and currencies are supported\?', 'Do you offer email hosting?'
$content = $content -replace 'CloudMeld Hosting connects with most major banks and supports multi-currency setups, making it ideal for international or multi-entity businesses\.', 'Yes. All CloudMeld Hosting plans include professional email hosting with your domain, with generous storage and security features.'

# Replace free trial FAQ
$content = $content -replace 'Is there a CloudMeld Hosting free version or trial\?', 'What technical support is included?'
$content = $content -replace 'Yes\. You can to pricing plans section to learn about our essential features and you can upgrade anytime as your needs gro.*', '24/7 technical support is included with every plan. Our expert team is always ready to help with setup, configuration, and troubleshooting.'

# Also update "Is my data encrypted" section
$content = $content -replace 'Is my data at risk with CloudMeld Hosting\?', 'Is my data secure?'
$content = $content -replace 'Yes\. CloudMeld Hosting uses bank-grade encryption and connects through certified APIs\. Your data is fully secured and never shared with third parties\.', 'Yes. CloudMeld Hosting uses enterprise-grade encryption, automated backups, and follows industry security standards to keep your data safe and secure.'

[System.IO.File]::WriteAllText($file, $content)
Write-Host "FAQ section updated!"
