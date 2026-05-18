from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def load_vector_store():

    # Load PDFs
    loader = PyPDFDirectoryLoader("data/pdfs")

    documents = loader.load()

    print(f"Loaded {len(documents)} pages")

    # Text Chunking
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create FAISS Vector Store
    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    print("FAISS vector store created")

    return vector_store