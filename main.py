import os
from typing import Annotated

import typer

from src.parsing import build_glossary_term_from_python_module, GlossaryTerm
from src.templating import templating_glossary_terms_to_markdown_list

app = typer.Typer()

@app.command()
def do(
        module_path: Annotated[str, typer.Option(help="path to the module to parse to generate a glossary from")]='tests.fixtures.domain.entities'
) -> str:
    glossary_terms: set[GlossaryTerm] = build_glossary_term_from_python_module(module_path)
    markdown_list = templating_glossary_terms_to_markdown_list(glossary_terms)
    current_directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(current_directory, 'glossary(list).md'), 'w') as f:
        f.write(markdown_list)
    print(markdown_list)
    return markdown_list


if __name__ == "__main__":
    app()