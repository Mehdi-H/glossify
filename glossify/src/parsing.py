import ast
import importlib
import inspect
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class GlossaryTerm:
    name: str
    doc: Optional[str] = None


def build_glossary_term_from_python_file(file_path: str) -> set[GlossaryTerm]:
    with open(file_path) as f:
        tree = ast.parse(f.read())
        classes: list[ast.ClassDef] = [n for n in tree.body if isinstance(n, ast.ClassDef)]
        return {
            GlossaryTerm(name=_class.name, doc=ast.get_docstring(_class))
            for _class in classes
            if ast.get_docstring(_class)
        }
