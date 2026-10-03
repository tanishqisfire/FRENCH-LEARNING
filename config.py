modelName = "llama3.1:8b"
level = "A1"
topic = "everyday life"

systemPrompt = ( "You are a French teacher. You write short, natural spoken French "
    "for pronunciation practice. Reply with only the French sentence, "
    "no translation, no quotes, no explanation.")

userPrompt = (
    "Write one random sentence in French at CEFR level {level} about the topic: "
    "{topic}. Maximum 15 words."
)