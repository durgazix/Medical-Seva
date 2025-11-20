# # PDF loaders (correct for LangChain 0.2+)
# from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

# # Text splitter
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# # Correct HuggingFace embeddings import
# from langchain_huggingface import HuggingFaceEmbeddings

# # Document class (updated location)
# from langchain_core.documents import Document

# from typing import List


# # Extract Data From PDF Folder
# def load_pdf_file(data):
#     loader = DirectoryLoader(
#         data,
#         glob="*.pdf",
#         loader_cls=PyPDFLoader
#     )
#     documents = loader.load()
#     return documents


# # Keep minimal metadata
# def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
#     minimal_docs: List[Document] = []
#     for doc in docs:
#         src = doc.metadata.get("source", "")
#         minimal_docs.append(
#             Document(
#                 page_content=doc.page_content,
#                 metadata={"source": src}
#             )
#         )
#     return minimal_docs


# # Split extracted text into chunks
# def text_split(extracted_data):
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=20
#     )
#     text_chunks = text_splitter.split_documents(extracted_data)
#     return text_chunks


# # Download or load embeddings
# def download_hugging_face_embeddings():
#     embeddings = HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2"
#     )
#     return embeddings



# PDF Loaders (LangChain 0.2+)

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

from typing import List

def load_pdf_file(data_path: str):
    """
    Loads all PDF files from a directory.
    """
    loader = DirectoryLoader(
        data_path,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    documents = loader.load()
    return documents

def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    """
    Simplifies each Document by keeping only page_content and source metadata.
    """
    minimal_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source", "")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
            )
        )
    return minimal_docs

def text_split(extracted_data: List[Document]):
    """
    Splits documents into chunks for embedding.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20
    )
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks


def download_hugging_face_embeddings():
    """
    Loads MiniLM embeddings (384-dim) used for Pinecone Vector Search.
    """
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embeddings
