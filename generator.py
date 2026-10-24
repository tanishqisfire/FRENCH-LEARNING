import re
import config

def _clean(text):
    text = re.sub(r"[«»\"—–]", "", text)
    text = re.sub(r"\s+([?!.,;:])", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()





def _messages():
    return[
        {"role":"system","content":config.systemPrompt},
        {"role":"user","content":config.userPrompt.format(level=config.level, topic=config.topic)},
    ]

def _generate_with_api():
    from openrouter import OpenRouter
    client = OpenRouter(api_key=config.apiKey, server_url=config.serverUrl)
    response = client.chat.send(
        model = config.modelName,
        messages = _messages(),
        temperature = 1.0,)
    return response.choices[0].message.content


def _generate_with_ollama():
    import ollama
    response = ollama.chat(
        model = config.ollamaModelName,
        messages = _messages(),
        options = {"temperature":1.0},
    )
    return response["message"]["content"]

def generate_sentence():
    if config.apiKey:
        try:
          text = _generate_with_api()
          if text and text.strip():
              return _clean(text)
          print("API returned an empty reply, switching to Ollama")
        except Exception as e:
            print("API failed, switching to Ollama:", e)
    text = _generate_with_ollama()
    return _clean(text or "")


