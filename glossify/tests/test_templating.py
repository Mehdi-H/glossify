from glossify.src.parsing import GlossaryTerm

from glossify.src.templating import templating_glossary_terms_to_markdown_list


def test_templating_glossary_term_to_markdown_list():
    assert templating_glossary_terms_to_markdown_list({
        GlossaryTerm(
            name="VariableMessageSign",
            doc="🚦 Represents a dynamic road sign used in smart traffic management systems.\n\nA Variable-message sign (VMS) is an electronic traffic sign used on roadways\nto give travelers information about traffic conditions, weather hazards,\nspecial events, or other important messages."
        )
    }) == """# Glossary

- VariableMessageSign: 🚦 Represents a dynamic road sign used in smart traffic management systems.\n\nA Variable-message sign (VMS) is an electronic traffic sign used on roadways\nto give travelers information about traffic conditions, weather hazards,\nspecial events, or other important messages.

"""


def test_templating_glossary_terms_to_markdown_list_produces_a_sorted_glossary():
    assert templating_glossary_terms_to_markdown_list({
        GlossaryTerm(
            name="VariableMessageSign",
            doc="🚦 Represents a dynamic road sign used in smart traffic management systems.\n\nA Variable-message sign (VMS) is an electronic traffic sign used on roadways\nto give travelers information about traffic conditions, weather hazards,\nspecial events, or other important messages."
        ),
        GlossaryTerm(
            name="StreetLamp",
            doc="💡 Represents a smart street lighting unit in an urban environment.\n\nA StreetLamp in a smart city context is an intelligent lighting fixture\nthat can be remotely controlled and monitored, often integrating additional\nsensors or capabilities."
        )
    }) == """# Glossary

- StreetLamp: 💡 Represents a smart street lighting unit in an urban environment.\n\nA StreetLamp in a smart city context is an intelligent lighting fixture\nthat can be remotely controlled and monitored, often integrating additional\nsensors or capabilities.
- VariableMessageSign: 🚦 Represents a dynamic road sign used in smart traffic management systems.\n\nA Variable-message sign (VMS) is an electronic traffic sign used on roadways\nto give travelers information about traffic conditions, weather hazards,\nspecial events, or other important messages.

"""
