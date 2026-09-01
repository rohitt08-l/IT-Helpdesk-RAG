from app.rag_pipeline import build_rag_pipeline
from langchain_core.output_parsers import StrOutputParser

retriever, llm = build_rag_pipeline()

parser = StrOutputParser()

while True:

    question = input("\nAsk Question: ")

    if question.lower() == "exit":
        break

    # Retrieve relevant documents
    docs = retriever.invoke(question)

    # Combine retrieved context
    context = "\n\n".join([doc.page_content for doc in docs])

    # Format the prompt
    final_prompt = f"""
You are an IT Helpdesk Assistant.

Answer only from the provided context.

Context:
{context}

Question:
{question}
"""

    # Generate answer
    response = llm.invoke(final_prompt)

    # Parse output
    answer = parser.invoke(response)

    print("\nAnswer:")
    print(answer)