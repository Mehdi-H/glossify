import os
from enum import StrEnum
from typing import Annotated

import typer

from glossify.src.parsing import GlossaryTerm, build_glossary_term_from_python_file
from glossify.src.templating import templating_glossary_terms_to_markdown_list, \
    templating_glossary_terms_to_markdown_table

app = typer.Typer()

current_directory = os.path.abspath(os.path.dirname(__file__))
demo_file_path = os.path.join(current_directory, 'tests/fixtures/domain/entities.py')

class OuputFormat(StrEnum):
    MD_LIST = "md_list"
    MD_TABLE = "md_table"


@app.command()
def main(
        file_path: Annotated[str, typer.Option(
            help="Path to the file to parse to generate a glossary from")] = demo_file_path,
        format: Annotated[OuputFormat, typer.Option(help="Output format")] = OuputFormat.MD_TABLE
) -> str:
    glossary_terms: set[GlossaryTerm] = build_glossary_term_from_python_file(file_path)
    if format == OuputFormat.MD_LIST:
        produced_glossary = templating_glossary_terms_to_markdown_list(glossary_terms)
    else:
        produced_glossary = templating_glossary_terms_to_markdown_table(glossary_terms)
    path_to_glossary_output = os.path.join(current_directory, f"glossary_{format}.md")
    with open(path_to_glossary_output, 'w') as f:
        f.write(produced_glossary)
    print(f"[*] Glossary generated successfully! @ file://{path_to_glossary_output}")
    return produced_glossary


if __name__ == "__main__":
    app()
