import ollama
import config


def generate_sentence():
    response = ollama.chat(model = config.modelName, messages = [ {"role": "system", "content": config.systemPrompt},
                                                                  {"role": "user", "content": config.userPrompt.format(level = config.level, topic=config.topic)},
    ] ,
    
    options = {"temperature": 1.0},
    )
    

    return response["message"]["content"].strip()



if __name__ == "__main__":
    print(generate_sentence())

