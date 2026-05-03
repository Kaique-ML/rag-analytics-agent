import os
import argparse
import pandas as pd
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders import DataFrameLoader
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description='Ingestão de dados para o Pinecone')
    parser.add_argument('--file', type=str, required=True, help='Caminho do arquivo CSV')
    args = parser.parse_args()

    # 1. Carregar Dados
    print(f"📂 Carregando {args.file}...")
    df = pd.read_csv(args.file)
    loader = DataFrameLoader(df, page_content_column=df.columns[0]) # Ajuste conforme a coluna principal
    documents = loader.load()

    # 2. Split (Opcional para CSVs pequenos, mas bom para contexto)
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # 3. Embeddings e Vector Store
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    index_name = os.getenv("PINECONE_INDEX")

    print(f"🚀 Enviando para o Pinecone (Index: {index_name})...")
    PineconeVectorStore.from_documents(docs, embeddings, index_name=index_name)
    print("✅ Ingestão concluída com sucesso!")

if __name__ == "__main__":
    main()