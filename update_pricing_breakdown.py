#!/usr/bin/env python3
"""Update Starter Hosting pricing to show breakdown: ₹7000 + 18% GST = ₹8260"""

import os

file_path = "c:\\Users\\abhis\\Documents\\Abhishek_Documents\\websites\\vercelhost\\index (1).html"

# Read the current file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Store original for comparison
original_size = len(content)

# The file contains non-breaking space (\xa0) instead of regular space
# Find and replace the Starter Hosting pricing section
old_pattern = '<div class="text-inline-wrapper"><div class="heading-style-2 no-margin">₹8260</div><div class="text-size-large text-style-muted">\xa0</div></div><div class="features-wrapper">'

new_pattern = '<div class="text-inline-wrapper"><div style="width:100%"><div class="heading-style-2 no-margin">₹8260</div><div class="text-size-small text-style-muted" style="margin-top:8px;"><strong>₹7,000</strong> + 18% GST = <strong>₹8,260</strong></div></div></div><div class="features-wrapper">'

# Perform replacement
if old_pattern in content:
    # Only replace the first occurrence (Starter Hosting)
    content = content.replace(old_pattern, new_pattern, 1)
    replacements = 1
    print(f"✓ Successfully replaced Starter Hosting pricing breakdown!")
else:
    print("✗ Could not find exact pattern with non-breaking space")
    replacements = 0

# Write the updated content
if replacements > 0:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    new_size = len(content)
    size_change = new_size - original_size
    
    print(f"\n✅ File updated successfully!")
    print(f"Original size: {original_size:,} characters")
    print(f"New size: {new_size:,} characters")
    print(f"Change: {size_change:+} characters")
    print(f"\nStarting Pricing: ₹7,000 + 18% GST = ₹8,260 ✓")
else:
    print("\n✗ No replacements made. Please check the file structure.")

