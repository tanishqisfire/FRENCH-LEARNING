from phonemizer import phonemize
from phonemizer.separator import Separator 


def text_to_phonemes(text, language="fr-fr"):
                   sep = Separator(phone=" ", word = " | ")
                   raw = phonemize(text, language = language, backend="espeak", separator=sep, strip=True, with_stress = False,)
                   words = []
                   for chunk in raw.split("|"):
                           phones = chunk.split()
                           if phones:
                                   words.append(phones)
                   return words
                   






def flatten_phonemes(words):
        flat = []
        word_ids = []
        for index, word in enumerate(words):
                for phone in word:
                        flat.append(phone)
                        word_ids.append(index)
        return flat, word_ids



