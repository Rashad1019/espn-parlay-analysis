with open('espn_parlay_analysis.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add CSS to hide output cells
css = """
<style>
.jp-OutputArea-output {
    display: none !important;
}
.jp-OutputArea-prompt {
    display: none !important;
}
.jp-OutputPrompt {
    display: none !important;
}
</style>
"""

content = content.replace('</head>', f'{css}</head>')

with open('espn_parlay_analysis.html', 'w', encoding='utf-8') as f:
    f.write(content) 