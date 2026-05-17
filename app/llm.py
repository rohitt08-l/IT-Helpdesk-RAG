from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


def load_llm():

    llm = ChatGroq(
        model="llama3-8b-8192",
        temperature=0
    )

    return llm