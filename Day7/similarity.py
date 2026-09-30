from sentence_transformers import util, SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
sentences=[
    "I love to play",
    "I love to watch movies",
    "I like to sleep"
]
sentence_embedding=model.encode(sentences)
similarity1 = util.cos_sim(sentence_embedding[0],sentence_embedding[1])
print(similarity1.item())