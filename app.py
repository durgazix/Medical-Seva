# from flask import Flask, render_template, jsonify, request
# from src.helper import download_hugging_face_embeddings
# from langchain_pinecone import PineconeVectorStore
# # from langchain_openai import ChatOpenAI
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.chains import create_retrieval_chain
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain_core.prompts import ChatPromptTemplate
# from dotenv import load_dotenv
# from src.prompt import *
# import os


# app = Flask(__name__)

# load_dotenv()

# PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
# # OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY')
# GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY')

# os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
# # os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
# os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


# embeddings = download_hugging_face_embeddings()

# index_name = "medical-chatbot" 
# # Embed each chunk and upsert the embeddings into your Pinecone index.
# docsearch = PineconeVectorStore.from_existing_index(
#     index_name=index_name,
#     embedding=embeddings
# )

# retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

# # chatModel = ChatOpenAI(model="gpt-4o")
# chatModel = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash")
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", system_prompt),
#         ("human", "{input}"),
#     ]
# )

# question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
# rag_chain = create_retrieval_chain(retriever, question_answer_chain)



# @app.route("/")
# def index():
#     return render_template('chat.html')



# @app.route("/get", methods=["GET", "POST"])
# def chat():
#     msg = request.form["msg"]
#     input = msg
#     print(input)
#     response = rag_chain.invoke({"input": msg})
#     print("Response : ", response["answer"])
#     return str(response["answer"])



# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port= 8080, debug= True)

from flask import Flask, render_template, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableLambda

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
from src.prompt import *
import os


app = Flask(__name__)

load_dotenv()

# API KEYS
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


# Load Embeddings
embeddings = download_hugging_face_embeddings()

# Pinecone index
index_name = "medical-chatbot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)


# Chat model (Gemini)
chatModel = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash")


# ---------- NEW LANGCHAIN RAG PIPELINE (2024) ----------
def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "User Question: {question}\n\nRelevant Context:\n{context}")
    ]
)


def get_question(x):
    return x["input"]

rag_chain = (
    {
        "question": RunnableLambda(get_question),
        "context": RunnableLambda(get_question) | retriever | format_docs
    }
    | prompt
    | chatModel
    | StrOutputParser()
)


@app.route("/")
def index():
    return render_template("chat.html")



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print("User:", msg)

    response = rag_chain.invoke({"input": msg})
    print("Response:", response)

    return str(response)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
