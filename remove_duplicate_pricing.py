import re

# File path
file_path = r"c:\Users\abhis\Documents\Abhishek_Documents\websites\vercelhost\index (1).html"

# Read file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original file size: {len(content)} characters")

# Find and remove the duplicate monthly pricing grid
# Pattern: <div class="w-layout-grid pricing-grid is-monthly slide-in-from-bottom">...</div></div></section>
# We need to match from the start of the duplicate grid to just before the closing </div></section> of the pricing section

# The duplicate starts with: <div class="w-layout-grid pricing-grid is-monthly slide-in-from-bottom">
# And it contains three complete pricing-plan divs + the closing tag
# It ends just before the </div></section> that closes the pricing section

# Let's use a careful regex to match this entire duplicate section
pattern = r'<div class="w-layout-grid pricing-grid is-monthly slide-in-from-bottom">.*?</div></div></div></section>'

# Count matches first
matches = re.findall(pattern, content, re.DOTALL)
print(f"Found {len(matches)} instances of monthly pricing grid pattern")

# If we find the pattern, we need to be more surgical
# The duplicate grid starts at opening and has 3 pricing cards
# Let's match specifically: the is-monthly grid div and everything until we hit the next </section> tag

# More specific pattern: match the is-monthly div with all its contents
monthly_grid_pattern = r'<div class="w-layout-grid pricing-grid is-monthly slide-in-from-bottom">.*?(?=</div></section>)'

# Remove the duplicate monthly grid
if 'pricing-grid is-monthly' in content:
    # Find the position of the duplicate
    start_marker = '<div class="w-layout-grid pricing-grid is-monthly slide-in-from-bottom">'
    start_pos = content.find(start_marker)
    
    if start_pos != -1:
        # Find the end of this div section - it ends with three </div></div></div> after the last pricing card
        # Look for the pattern after the start
        search_from = start_pos + len(start_marker)
        
        # The duplicate section structure:
        # <div class="w-layout-grid pricing-grid is-monthly...">
        #   <div class="pricing-plan">...</div>  (card 1)
        #   <div class="pricing-plan">...</div>  (card 2)
        #   <div class="pricing-plan">...</div>  (card 3)
        # </div>  <-- this closes the grid
        
        # We need to find where this grid div closes
        # Count divs: +1 for each opening, -1 for each closing
        div_count = 1  # Starting with the grid div itself
        pos = search_from
        
        while div_count > 0 and pos < len(content):
            next_open = content.find('<div', pos)
            next_close = content.find('</div>', pos)
            
            if next_close == -1:
                break
            
            if next_open != -1 and next_open < next_close:
                div_count += 1
                pos = next_open + 4
            else:
                div_count -= 1
                pos = next_close + 6
                if div_count == 0:
                    # Found the closing div
                    end_pos = pos
                    break
        
        if div_count == 0:
            # Remove the duplicate section
            content_before = content[:start_pos]
            content_after = content[end_pos:]
            content = content_before + content_after
            print(f"✓ Removed duplicate monthly pricing grid ({end_pos - start_pos} characters)")
        else:
            print("✗ Could not find proper closing tag for duplicate grid")
    else:
        print("✗ Could not find duplicate monthly pricing grid")
else:
    print("No duplicate monthly pricing grid found - already removed!")

print(f"Updated file size: {len(content)} characters")

# Write file
with open(file_path, 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print("✓ SUCCESS: Duplicate pricing grid removed!")
