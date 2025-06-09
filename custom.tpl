{% extends "basic/index.html.j2" %}

{# Remove input cells #}
{% block input %}
{% endblock input %}

{# Remove output cells except for plots and markdown #}
{% block output %}
    {% if output.output_type == 'display_data' and 'image/png' in output.data %}
        {{ super() }}
    {% endif %}
{% endblock output %}

{# Keep markdown cells #}
{% block markdowncell %}
    {{ super() }}
{% endblock markdowncell %}

{# Custom CSS to clean up the styling #}
{% block header %}
<style>
    .jp-OutputArea-output {
        background-color: white !important;
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    .jp-RenderedImage {
        display: block;
        margin: 20px auto;
    }
    body {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
        font-family: Arial, sans-serif;
    }
    h1, h2, h3 {
        color: #333;
    }
</style>
{% endblock header %} 