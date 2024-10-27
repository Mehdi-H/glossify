from src.parsing import GlossaryTerm, build_glossary_term_from_python_module


def test_build_glossary_term_from_python_module():
    assert build_glossary_term_from_python_module('tests.fixtures.domain.an_entity') == {
        GlossaryTerm(
            name="VariableMessageSign",
            doc="🚦 Represents a dynamic road sign used in smart traffic management systems.\n\nA Variable-message sign (VMS) is an electronic traffic sign used on roadways\nto give travelers information about traffic conditions, weather hazards,\nspecial events, or other important messages."
        ),
    }


def test_build_glossary_terms_from_python_module():
    assert build_glossary_term_from_python_module('tests.fixtures.domain.entities') == {
        GlossaryTerm(
            name="VariableMessageSign",
            doc="🚦 Represents a dynamic road sign used in smart traffic management systems.\n\nA Variable-message sign (VMS) is an electronic traffic sign used on roadways\nto give travelers information about traffic conditions, weather hazards,\nspecial events, or other important messages."
        ),
        GlossaryTerm(
            name="StreetLamp",
            doc="💡 Represents a smart street lighting unit in an urban environment.\n\nA StreetLamp in a smart city context is an intelligent lighting fixture\nthat can be remotely controlled and monitored, often integrating additional\nsensors or capabilities."
        ),
        GlossaryTerm(
            name="ElectricalCabinet",
            doc="⚡ Represents an electrical distribution cabinet in the smart city infrastructure.\n\nAn ElectricalCabinet is a key component in the city's power distribution\nnetwork, often upgraded with smart capabilities for remote monitoring\nand management."
        ),
        GlossaryTerm(
            name="AirQualitySensor",
            doc="🌫 Represents a sensor device for monitoring air quality in urban environments.\n\nAn AirQualitySensor is part of the environmental monitoring network in a\nsmart city, providing real-time data on various air quality parameters."
        ),
        GlossaryTerm(
            name="TrafficFlowSensor",
            doc="🚗 Represents a sensor for monitoring and analyzing traffic flow in urban areas.\n\nA TrafficFlowSensor is a crucial component in smart traffic management systems,\nproviding real-time data on vehicle movement, density, and speed."
        ),
    }

