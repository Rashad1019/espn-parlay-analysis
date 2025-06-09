import re

# Read the HTML file
with open('espn_parlay_analysis.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Remove paragraph marks and any related HTML entities
content = re.sub(r'[¶]|&para;|&#182;|&#xB6;', '', content)

# Write the cleaned content back
with open('clean_espn_parlay_analysis.html', 'w', encoding='utf-8') as file:
    file.write(content) 