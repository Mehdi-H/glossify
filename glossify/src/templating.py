import os

from jinja2 import Environment, FileSystemLoader

from glossify.src.parsing import GlossaryTerm


def templating_glossary_terms_to_markdown_list(glossary_terms: set[GlossaryTerm]) -> str:
    sorted_glossary_terms = sorted(glossary_terms, key=lambda term: term.name)
    current_directory = os.path.abspath(os.path.dirname(__file__))
    environment = Environment(loader=FileSystemLoader(os.path.join(current_directory, "templates/")))
    template = environment.get_template("glossary_as_markdown_list.md")
    return template.render(
        glossary_terms=sorted_glossary_terms,
    )
