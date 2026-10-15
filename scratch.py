from phonemes import text_to_phonemes, flatten_phonemes
from listen import hear_phonemes
from pipeline import check_pronounciation


sentence = "Je vais à l'école avec ma famille."
words = text_to_phonemes(sentence)
ref, word_ids = flatten_phonemes(words)
heard = hear_phonemes("recording.wav")

print("REF  :", ref)
print("HEARD:", heard)

for r in check_pronounciation(sentence, "recording.wav"):
    print(r["word"], r["ok"], r["problems"])