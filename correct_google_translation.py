from translation_chain_types import ChainTypes
from googletrans import Translator
import random


def get_random_languages_chain():
    return random.choice(list(ChainTypes)).value


def get_translated_text(text_to_custom):
    translator = Translator()
    for i in get_random_languages_chain():
        text_to_custom = translator.translate(text_to_custom, src=i[0], dest=i[1]).text
    return text_to_custom
