# Glossary

| Term | Meaning |
|:----:|:--------|
{% for term in glossary_terms -%}
| {{ term.name }} | {{ term.doc -}} |
{% endfor %}

