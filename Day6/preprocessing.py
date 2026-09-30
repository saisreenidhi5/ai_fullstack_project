import ollama
import chromadb 
# Embedding model using Ollama
model = "nomic-embed-text"
with open("ai_sample.txt", "r") as file:
    text = file.read()
#print(text)
#print("No of characters: ", len(text))
chunks = []
chunk_size = 30 #20,30,50
chunk_overlap = 10 #5, 15, 30
step = chunk_size - chunk_overlap
for i in range(0,len(text),step):
    chunk = text[i:i+chunk_size]
    chunks.append(chunk)
#print("No of chunks:", len(chunks))
#for i in range(len(chunks)):
    #print(f"chunk {i} -> {chunks[i]}")
#for chunk in chunks:
    #print(chunk)
#Embeddings
document_chunks = [
    "search_document: " + chunk
    for chunk in chunks
]
response = ollama.embed(
    model=model,
    input=document_chunks
)
embeddings = response["embeddings"]
#print("Embeddings created successfully.")
#print("No of embeddings:", len(embeddings))
#print(embeddings[0])
#print(len(embeddings[0]))
#Chroma db
client = chromadb.Client()
collection = client.create_collection(name="My_documents")
print("Collection created successfully.")
ids = []
for i in range(len(chunks)):
    ids.append(str(i))
collection.add(
    ids=ids,
    documents=chunks,
    embeddings=embeddings
)
#print("No of collections:",collection.count())
results = collection.get()
for i in range(len(results["ids"])):
    print(f"ID: {results['ids'][i]} -> Chunk:{results['documents'][i]}")
chunk1 = collection.get(ids=['0'])
print("chunk1")
col = collection.get(ids=['0'])
print(col)