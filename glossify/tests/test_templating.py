from glossify.src.parsing import GlossaryTerm

from glossify.src.templating import templating_glossary_terms_to_markdown_list, \
    templating_glossary_terms_to_markdown_table


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


def test_templating_glossary_term_to_markdown_table():
    assert templating_glossary_terms_to_markdown_table({
        GlossaryTerm(
            name="VariableMessageSign",
            doc="🚦 Represents a dynamic road sign used in smart traffic management systems.\n\nA Variable-message sign (VMS) is an electronic traffic sign used on roadways\nto give travelers information about traffic conditions, weather hazards,\nspecial events, or other important messages."
        )
    }) == """# Glossary

| Term | Meaning |
|:----:|:--------|
| VariableMessageSign | 🚦 Represents a dynamic road sign used in smart traffic management systems.<br><br>A Variable-message sign (VMS) is an electronic traffic sign used on roadways<br>to give travelers information about traffic conditions, weather hazards,<br>special events, or other important messages.|

"""

def test_templating_glossary_terms_to_markdown_table_produces_a_sorted_glossary():
    assert templating_glossary_terms_to_markdown_table({
        GlossaryTerm(
            name="VariableMessageSign",
            doc="🚦 Represents a dynamic road sign used in smart traffic management systems.\n\nA Variable-message sign (VMS) is an electronic traffic sign used on roadways\nto give travelers information about traffic conditions, weather hazards,\nspecial events, or other important messages."
        ),
        GlossaryTerm(
            name="StreetLamp",
            doc="💡 Represents a smart street lighting unit in an urban environment.\n\nA StreetLamp in a smart city context is an intelligent lighting fixture\nthat can be remotely controlled and monitored, often integrating additional\nsensors or capabilities."
        )
    }) == """# Glossary

| Term | Meaning |
|:----:|:--------|
| StreetLamp | 💡 Represents a smart street lighting unit in an urban environment.<br><br>A StreetLamp in a smart city context is an intelligent lighting fixture<br>that can be remotely controlled and monitored, often integrating additional<br>sensors or capabilities.|
| VariableMessageSign | 🚦 Represents a dynamic road sign used in smart traffic management systems.<br><br>A Variable-message sign (VMS) is an electronic traffic sign used on roadways<br>to give travelers information about traffic conditions, weather hazards,<br>special events, or other important messages.|

"""
