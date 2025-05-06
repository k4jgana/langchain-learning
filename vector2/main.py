from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from langchain import hub
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain




if __name__=="__main__":
    load_dotenv()
    pdf_path = "D:\\lang\\ice_breaker\\vector2\\2210.03629v3.pdf"
    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=30, separator="\n")
    docs = text_splitter.split_documents(documents=documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local('faiss_index_react')

    vectorstore = FAISS.load_local(
        "faiss_index_react", embeddings, allow_dangerous_deserialization=True
    )

    retrieval_qa_chat_prompt = hub.pull('langchain-ai/retrieval-qa-chat')
    combine_docs_chain = create_stuff_documents_chain(ChatOpenAI(), retrieval_qa_chat_prompt)

    retrieval_chain = create_retrieval_chain(vectorstore.as_retriever(), combine_docs_chain)

    res = retrieval_chain.invoke({"input": "Give a short summary about ReAct"})

    print(res['answer'])



