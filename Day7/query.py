from sentence_transformers import SentenceTransformer
import chromadb, ollama
model = SentenceTransformer("all-MiniLM-L6-v2")
file_name = "sample1.txt"
with open("sample1.txt", "r") as file:

    text = file.read()
chunks = []

chunk_size = 30 #20,30,50

chunk_overlap = 10 #5, 15, 30

step = chunk_size - chunk_overlap

for i in range(0,len(text),step):

    chunk = text[i:i+chunk_size]

    chunks.append(chunk)
embeddings = model.encode(chunks)
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="My_document")
ids = []

for i in range(len(chunks)):

    ids.append(f"{file_name}_{i}")

collection.add(

    ids=ids,

    documents=chunks,

    embeddings=embeddings.tolist()

)
#Query
question =input("Ask a question..")
#converting to vector
question_embedding = model.encode(question)
#searching for this question in db
results= collection.query(
    query_embeddings=[question_embedding.tolist()],
    n_results=3
)
retrieved_results=results['documents'][0]
retrieved_ids=results['ids'][0]
#prompting
context='\n'.join(retrieved_results)
prompt=f'''
Answer the question using the context provided below.
Question:{question}
Context:{context}
Answer:
'''
#Connecting to local model
response=ollama.chat(
        model="llama3.2:3b",
        messages=[{
            "role":"user",
            "content":prompt
        }]
)
print(response['message']['content'])