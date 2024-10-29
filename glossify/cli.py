import os
from typing import Annotated

import typer

from glossify.src.parsing import GlossaryTerm, build_glossary_term_from_python_file
from glossify.src.templating import templating_glossary_terms_to_markdown_list

app = typer.Typer()

current_directory = os.path.abspath(os.path.dirname(__file__))
demo_file_path = os.path.join(current_directory, 'tests/fixtures/domain/entities.py')


@app.command()
def main(
        file_path: Annotated[str, typer.Option(
            help="Path to the file to parse to generate a glossary from")] = demo_file_path
) -> str:
    glossary_terms: set[GlossaryTerm] = build_glossary_term_from_python_file(file_path)
    markdown_list = templating_glossary_terms_to_markdown_list(glossary_terms)
    path_to_glossary_output = os.path.join(current_directory, 'glossary_as_list.md')
    with open(path_to_glossary_output, 'w') as f:
        f.write(markdown_list)
    print(f"[*] Glossary list generated successfully! @ file://{path_to_glossary_output}")
    return markdown_list


if __name__ == "__main__":
    app()
