from app.llm import load_llm
from app.vector_store import load_vector_store
from app.prompt_template import prompt


def build_rag_pipeline():

    llm = load_llm()

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    print("RAG pipeline ready")

    return retriever, llm