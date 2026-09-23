import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content":"what is GenZ in 2 lines"
        }
    ]
)
print(response["message"]["content"]) 