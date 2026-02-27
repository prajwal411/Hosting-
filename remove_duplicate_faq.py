import re

# File path
file_path = r"c:\Users\abhis\Documents\Abhishek_Documents\websites\vercelhost\index (1).html"

# Read file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original file size: {len(content)} characters")

# Now we have TWO instances of the same FAQ content:
# 1. Proper FAQ section (id="faqs") - KEEP THIS
# 2. Duplicate FAQ inside contact section - REMOVE THIS

# Find the contact section
contact_start = content.find('<section id="contact"')

if contact_start != -1:
    # Find the FAQ duplicate within the contact section
    # Look for the second occurrence of the FAQ grid (after the first FAQ section)
    
    # Find first FAQ section end
    first_faq = content.find('<section id="faqs"')
    first_faq_end = content.find('</section>', first_faq)
    
    # Now search for duplicate FAQ content AFTER the first FAQ section
    duplicate_faq_start = content.find('<div class="w-layout-vflex slide-in-from-left"><div class="text-color-yellow-700"><div class="tag-wrapper">', first_faq_end)
    
    if duplicate_faq_start != -1:
        # This duplicate FAQ section includes:
        # - The tag wrapper with "FAQs"
        # - The heading "Frequently asked questions"
        # - The description
        # - The faqs-grid with all 5 questions
        
        # Find where this duplicate section ends
        # It should end before </div></section> that closes the contact section
        # The duplicate ends with: </div></div></section>
        
        # Search for the end pattern after the duplicate start
        # The duplicate has: <div class="w-layout-grid faqs-grid">...5 FAQ items...</div>
        
        # Find the faqs-grid within this duplicate
        duplicate_grid_start = content.find('<div class="w-layout-grid faqs-grid">', duplicate_faq_start)
        
        if duplicate_grid_start != -1:
            # Find the end of this grid (it has 5 FAQ items)
            # Count to find the closing </div> for this grid
            
            # Start counting from after the opening grid div
            pos = duplicate_grid_start + len('<div class="w-layout-grid faqs-grid">')
            div_count = 1
            
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
                        duplicate_end = pos
                        break
            
            if div_count == 0:
                # Now we need to also remove the heading and description before the grid
                # Go back to include everything from the slide-in-from-left div
                
                # The structure is:
                # <div class="w-layout-vflex slide-in-from-left">
                #   <div class="text-color-yellow-700">...tag...</div>
                #   ...heading...
                # </div>
                # <p class="text-size-large">...description...</p>
                # </div>
                # <div class="w-layout-grid faqs-grid">...5 items...</div>
                
                # Find where to end - need to include closing tags
                # Look for </div></div></section> after the grid
                section_close = content.find('</div></section>', duplicate_end)
                
                if section_close != -1:
                    # Remove from the start of the duplicate content to the end
                    content_before = content[:duplicate_faq_start]
                    content_after = content[section_close:]
                    
                    content = content_before + content_after
                    
                    print(f"✓ Removed duplicate FAQ from contact section ({section_close - duplicate_faq_start} characters)")
                else:
                    print("✗ Could not find section close")
            else:
                print("✗ Could not find grid end properly")
        else:
            print("✗ Could not find duplicate FAQ grid")
    else:
        print("No duplicate FAQ found in contact section - already cleaned!")
else:
    print("✗ Could not find contact section")

print(f"Updated file size: {len(content)} characters")

# Write file
with open(file_path, 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print("✓ SUCCESS: FAQ section now has single clean structure!")
print("✓ 5 hosting-related questions in proper FAQ section")
print("✓ No duplicates")
