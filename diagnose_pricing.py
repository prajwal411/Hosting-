#!/usr/bin/env python3
"""Diagnose the exact whitespace in the pricing section"""

import os

file_path = "c:\\Users\\abhis\\Documents\\Abhishek_Documents\\websites\\vercelhost\\index (1).html"

# Read the current file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the section with Starter Hosting pricing
start_idx = content.find("Starter Hosting")
if start_idx != -1:
    # Get 500 chars around this section
    section = content[start_idx:start_idx + 600]
    
    # Look for the price pattern
    price_idx = section.find("₹8260")
    if price_idx != -1:
        # Get context around price
        context_start = max(0, price_idx - 100)
        context_end = min(len(section), price_idx + 200)
        context = section[context_start:context_end]
        
        print("=== Context around ₹8260 ===")
        print(repr(context))
        print("\n=== Readable format ===")
        print(context)
        
        # Show byte representation
        print("\n=== Byte representation ===")
        for i, char in enumerate(context):
            if char in [' ', '\n', '\t', '\r']:
                print(f"Pos {i}: {repr(char)} (whitespace)")
            else:
                print(f"Pos {i}: {char}")
