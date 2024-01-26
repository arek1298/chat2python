import openai
openai.api_key = "sk-xyz"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [
        {
            "role": "user",
            "content": "dame una lista de proyectos para crear con python"
        }
    ],
)

print(response)