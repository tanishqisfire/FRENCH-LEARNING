from openrouter import OpenRouter
import config

client = OpenRouter(
    api_key = config.apiKey,
    server_url = config.serverUrl
)
def generate_sentence():
    response = client.chat.send(model = config.modelName, messages = [ {"role": "system", "content": config.systemPrompt},
                                                                  {"role": "user", "content": config.userPrompt.format(level = config.level, topic=config.topic)},
    ] ,
    
    temperature = 1.0,
    )
    
    text = response.choices[0].message.content
    return (text or "").strip().strip('"')



