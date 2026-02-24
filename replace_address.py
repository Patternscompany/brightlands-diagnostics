import os
import re

directory = "."
modified_files = 0

new_address = "9-4-84/19, Near Olive Hospital Nanal nagar X road, road, Kakatiya Nagar, Golconda Fort, Hyderabad, Telangana 500008"

# Order matters: from most specific to least specific
replacements = [
    (r'6391 Elgin St\. Celina, Delaware New York\. USA', new_address),
    (r'9-4-84/19, Full Building, Near Olive\s*Hospital, Kakatiya Nagar, Hyderabad - 500008', new_address),
    (r'9-4-84/19, Near Olive Hospital, Kakatiya Nagar, Hyderabad - 500008', new_address),
    (r'9-4-84/19, Near Olive Hospital, Hyderabad\s*-\s*500008', new_address),
    (r'9-4-84/19, Near Olive Hospital, Hyderabad\.', new_address + '.'),
    (r'9-4-84/19, Near Olive Hospital, Hyderabad(?!\s*-|\.)', new_address),
]

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        original_content = f.read()

    content = original_content
    
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".html"):
            filepath = os.path.join(root, filename)
            if replace_in_file(filepath):
                modified_files += 1
                
print(f"Modified {modified_files} HTML files.")
