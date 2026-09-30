import ollama
import streamlit as st 
st.title(":yellow[Welcome to my ChatBot App 🤖!!!]")
st.subheader("✨Ask Questions 🌍Explore 📚Improve knowledge")
with st.sidebar:   
    st.header(":blue[Chat Settings⚙️]")
    if st.button("clear history 🗑️"):
        st.session_state.messages=[]
        st.success("Chat cleared✅")
    personalities={
        "Kid👶": "answer like you are explaing to a 5 year old kid in 2 lines only and include emojis",
        "Friend🫂": "answer in friendly and casual manner. give answer in 2 lines only",
        "Teacher🧑‍🏫": "answer like a professional teacher in that topic. give answer in 2 lines only"
        }
    personality = st.selectbox("Select a personality",personalities.keys())
    uploaded_file=st.file_uploader("Upload a text file..")
    try:
        if uploaded_file:
            context = uploaded_file.read().decode("utf-8")
            st.success("File uploaded successfully!👍")
            if st.button("Display"):
                st.text(context)
                st.snow()
                
    except:
        st.error("It's not text file")
        
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("You:")
if question:
    st.session_state.messages.append(
            {"role" : "user",
            "content" : question}
        )
    with st.chat_message("user"):
        st.write(question)
    with st.spinner("Thinking🤔..."):
        response = ollama.chat(
                model = "llama3.2:3b",
                messages = [
                    {"role": "system","content": personalities[personality]}]
                    +st.session_state.messages)
    st.session_state.messages.append(
            {"role":"assistant",
            "content":response["message"]["content"]
            }
        )
    with st.chat_message("assistant"):
        st.write(response["message"]["content"])

    