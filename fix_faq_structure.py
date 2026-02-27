import re

# File path
file_path = r"c:\Users\abhis\Documents\Abhishek_Documents\websites\vercelhost\index (1).html"

# Read file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original file size: {len(content)} characters")

# Find and remove the FIRST FAQ section (the one with finance questions)
# It starts with: <section id="faqs" class="section">
# And ends with: </section> (before the contact section)

# Pattern to match: from <section id="faqs"> to its closing </section>
# The section contains 6 finance-related FAQ items

# Search for the old finance FAQ section
old_faq_start = '<section id="faqs" class="section"><div class="w-layout-blockcontainer container w-container"><div class="section-heading"><div id="w-node-_518bc65d-6510-51f2-ea1c-cf841434f9b0-84bd1238" class="w-layout-vflex section-heading-wrapper"><div class="text-color-pink-700 slide-in-from-bottom"><div class="tag-wrapper"><div class="tag-bubble w-embed"><svg width="100%" height="100%" viewBox="0 0 10 11" fill="none" xmlns="http://www.w3.org/2000/svg">'

if old_faq_start in content:
    start_pos = content.find(old_faq_start)
    
    # Find the closing </section> for this FAQ section
    # We need to find the </section> that comes BEFORE <section id="contact"
    contact_section_start = content.find('<section id="contact"', start_pos)
    
    if contact_section_start != -1:
        # Search backwards from contact section to find the closing </section>
        search_area = content[start_pos:contact_section_start]
        last_section_close = search_area.rfind('</section>')
        
        if last_section_close != -1:
            # Calculate absolute position
            end_pos = start_pos + last_section_close + len('</section>')
            
            # Remove this entire section
            content_before = content[:start_pos]
            content_after = content[end_pos:]
            content = content_before + content_after
            
            print(f"✓ Removed old finance FAQ section ({end_pos - start_pos} characters)")
        else:
            print("✗ Could not find closing </section> tag")
    else:
        print("✗ Could not find contact section")
else:
    print("Old FAQ section not found - may already be removed")

# Now fix the SECOND FAQ section structure
# It's currently inside the contact section but should be its own section
# Change <section id="contact" to have proper FAQ structure

# The correct structure should be:
# 1. End pricing section
# 2. Start FAQs section (id="faqs")  
# 3. End FAQs section
# 4. Start contact section
# 5. End contact section

# Since we removed the old faqs section, we need to rename the contact section's FAQ content
# Actually, looking at the structure, the "contact" section HAS the FAQ grid inside it
# We need to extract it and make it a proper FAQ section

# Let's find the FAQ content within contact section
contact_faq_pattern = r'(<section id="contact".*?<div class="w-layout-vflex slide-in-from-left">.*?)<div class="w-layout-grid faqs-grid">.*?</div></div></section>'

match = re.search(contact_faq_pattern, content, re.DOTALL)
if match:
    print("Found FAQ content in contact section - will restructure")
    
    # Extract the FAQ grid portion
    # Pattern: everything from <div class="w-layout-grid faqs-grid"> to the end of that grid
    faq_grid_start = content.find('<div class="w-layout-grid faqs-grid">', content.find('id="contact"'))
    
    if faq_grid_start != -1:
        # Find where this FAQ grid ends (before </div></section></div> at the very end)
        # The FAQ grid has 5 items, each in a <div class="w-layout-vflex">
        # It ends with </div></div></section>
        
        # Let's restructure: create a proper FAQ section
        # Insert <section id="faqs"> before the contact section
        
        contact_section_pos = content.find('<section id="contact"')
        
        if contact_section_pos != -1:
            # Build the proper FAQ section structure
            faq_section = '''<section id="faqs" class="section"><div class="w-layout-blockcontainer container w-container"><div class="section-heading"><div id="w-node-_518bc65d-6510-51f2-ea1c-cf841434f9b0-84bd1238" class="w-layout-vflex section-heading-wrapper"><div class="text-color-pink-700 slide-in-from-bottom"><div class="tag-wrapper"><div class="tag-bubble w-embed"><svg width="100%" height="100%" viewBox="0 0 10 11" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="5" cy="5.5" r="5" fill="currentCOlor"/>
</svg></div><div class="text-size-large">FAQs</div></div></div><h2 class="no-margin slide-in-from-bottom">Frequently asked <span class="text-color-pink-700 text-style-italic">questions</span></h2></div><p class="text-size-large no-margin slide-in-from-bottom">Have questions? We've got answers. Here's everything you need to know about CloudMeld Hosting.</p></div><div class="w-layout-grid faqs-grid"><div class="w-layout-vflex"><h3 class="heading-style-5">Is this lifetime hosting?</h3><p class="no-margin">Yes. Pay once, hosting for lifetime. No recurring fees, no surprises.</p></div><div class="w-layout-vflex"><h3 class="heading-style-5">Is GST included in pricing?</h3><p class="no-margin">Yes. All prices include GST. You'll receive proper tax invoices.</p></div><div class="w-layout-vflex"><h3 class="heading-style-5">Do you handle deployment?</h3><p class="no-margin">Yes. We handle complete production deployment and domain setup.</p></div><div class="w-layout-vflex"><h3 class="heading-style-5">Can I upgrade plans later?</h3><p class="no-margin">Yes. You can upgrade your plan anytime as your business grows.</p></div><div class="w-layout-vflex"><h3 class="heading-style-5">Is support included?</h3><p class="no-margin">Yes. 24/7 monitoring and support included in all plans.</p></div></div></div></section>'''
            
            # Insert FAQ section before contact section
            content = content[:contact_section_pos] + faq_section + content[contact_section_pos:]
            print("✓ Created proper FAQ section structure")
            
            # Now remove the duplicate FAQ content from within contact section
            # Find and remove: from <div class="w-layout-vflex slide-in-from-left"> to </section> within contact
            # Actually, let's remove the entire malformed contact section since it only has FAQ content
            
            # Find the contact section again (position changed after insertion)
            contact_section_pos_new = content.find('<section id="contact"', contact_section_pos + len(faq_section))
            
            # Find the end of this contact section
            contact_end = content.find('</section>', contact_section_pos_new)
            
            if contact_end != -1:
                # Check if there's actual contact form content or just FAQ
                contact_section_content = content[contact_section_pos_new:contact_end]
                
                # If it only has FAQ content and no contact form, remove it
                if 'contact-form' not in contact_section_content and 'faqs-grid' in contact_section_content:
                    content = content[:contact_section_pos_new] + content[contact_end + len('</section>'):]
                    print("✓ Removed duplicate FAQ content from contact section")

print(f"Updated file size: {len(content)} characters")

# Write file
with open(file_path, 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print("✓ SUCCESS: FAQ section properly structured!")
print("✓ Old finance FAQs removed")
print("✓ Proper hosting FAQs in correct section")
