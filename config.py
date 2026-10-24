import os

modelName = "nvidia/nemotron-3.5-super-vl"
serverUrl = "https://ai.hackclub.com/proxy/v1"

apiKey = "".join(c for c in os.environ.get("LLM_API_KEY", "") if c.isascii() and c.isprintable()) or None

ollamaModelName = "llama3.1:8b"



level = "A1"
topic = "everyday life/school/work/ai/family/complementing"

systemPrompt = ( "You are a French teacher. You write short, natural spoken French "
    "for pronunciation practice. Reply with only the French sentence, "
    "no translation, no quotes, no explanation."
    "none at all very important")

userPrompt = (
    "Write one random sentence in French at CEFR level {level} about the topic: "
    "{topic}. Maximum 15 words and keep it very easy and simple. "
    "Formatting rules: write punctuation directly attached to the previous word, "
    "with no space before it (write 'Tu viens?' and never 'Tu viens ?'). "
    "Use only letters, apostrophes, hyphens and a final . ? or !. "
    "Do not use quotation marks, guillemets, dashes, ellipses, parentheses, "
    "emojis or digits. Do not use the phrase 'qu'est-ce que' and do not end a "
    "word with '-y'."
)


