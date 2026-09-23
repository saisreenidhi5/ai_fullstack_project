import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content":"what is Ai definition in 1 line, name types of ai,give examples of it with description of 1 line "
        }
    ]
)
print(response["message"]["content"]) 