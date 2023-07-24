from deep_translator import MyMemoryTranslator

"""
translator
"""

def english_to_french(english_text):
    """
    e2f
    """
    french_text = MyMemoryTranslator(
        source="english", target="french").translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    f2e
    """
    english_text = MyMemoryTranslator(
        source="french", target="english").translate(french_text)
    return english_text
