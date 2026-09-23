import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content":"what is Ai in 5 lines"
        }
    ]
)
print(response["message"]["content"]) 