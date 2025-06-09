import pdfkit

# Convert HTML to PDF
try:
    pdfkit.from_file('espn_parlay_analysis.html', 'espn_parlay_analysis.pdf')
except OSError:
    print("Please install wkhtmltopdf first from: https://wkhtmltopdf.org/downloads.html")
    print("After installing, try running this script again.") 