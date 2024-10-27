import importlib
import inspect
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class GlossaryTerm:
    name: str
    doc: Optional[str] = None


def build_glossary_term_from_python_module(module_path: str) -> set[GlossaryTerm]:
    return {
        GlossaryTerm(name=name, doc=inspect.getdoc(cls))
        for name, cls
        in inspect.getmembers(importlib.import_module(module_path), inspect.isclass)
    }
