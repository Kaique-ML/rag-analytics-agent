import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains import RetrievalQA

def get_rag_chain():
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = PineconeVectorStore(
        index_name=os.getenv("PINECONE_INDEX"), 
        embedding=embeddings
    )
    
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )