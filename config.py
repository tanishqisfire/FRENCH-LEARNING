import os

modelName = "nvidia/nemotron-3.5-super-vl"
serverUrl = "https://ai.hackclub.com/proxy/v1"

apiKey = os.environ.get("LLM_API_KEY")
level = "A1"
topic = "everyday life/school/work/ai/family/complementing"

systemPrompt = ( "You are a French teacher. You write short, natural spoken French "
    "for pronunciation practice. Reply with only the French sentence, "
    "no translation, no quotes, no explanation."
    "none at all very important")

userPrompt = (
    "Write one random sentence in French at CEFR level {level} about the topic: "
    "{topic}. Maximum 15 words and keep it very easy and simple"
)

apiKey = "".join(c for c in os.environ.get("LLM_API_KEY", "") if c.isascii() and c.isprintable())