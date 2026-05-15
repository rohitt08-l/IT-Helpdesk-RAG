from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    template=\"\"\"
You are an IT Helpdesk Assistant.

Answer only from the provided context.

If the answer is unavailable, say:
'I could not find this information in the knowledge base.'

Context:
{context}

Question:
{question}
\"\"\",
    input_variables=[\"context\", \"question\"]
)