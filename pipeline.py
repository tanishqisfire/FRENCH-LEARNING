from phonemes import text_to_phonemes, flatten_phonemes

from listen import hear_phonemes
from compare import build_grid, trace_back, summarize_words

def check_pronounciation(sentence, audio_path):
    words = text_to_phonemes(sentence)
    ref, word_ids = flatten_phonemes(words)
    heard = hear_phonemes(audio_path)
    grid = build_grid(ref, heard)
    steps = trace_back(ref, heard, grid)
    problems = summarize_words(steps, ref, word_ids, len(words))

    results = []

    for index, word in enumerate(words):
        results.append({"word": index, "phonemes": " ".join(word), "problems": problems[index], "ok": len(problems[index]) == 0,})

    return results