import re

# Read the HTML file
with open('espn_parlay_analysis.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Read the CSS file
with open('custom_style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Insert the CSS into the HTML
content = content.replace('</head>', f'<style>{css}</style></head>')

# Write the modified HTML
with open('espn_parlay_analysis.html', 'w', encoding='utf-8') as f:
    f.write(content) 