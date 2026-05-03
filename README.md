# 🤖 RAG Analytics Agent
> Pergunte seus dados em linguagem natural — LangChain + Pinecone + GPT-4o

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.2-1C3C3C)](https://langchain.com)
[![OpenAI](https://img.shields.io/badge/GPT--4o-OpenAI-412991?logo=openai&logoColor=white)](https://openai.com)
[![Pinecone](https://img.shields.io/badge/Pinecone-VectorDB-02D26F)](https://pinecone.io)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Demo](https://img.shields.io/badge/🚀_Demo-Online-00C851)](https://gabriel-rag-agent.streamlit.app)

## 🎯 Sobre

Agente de análise de dados que responde perguntas em **português natural** sobre relatórios, planilhas e documentos PDF. Combina RAG (Retrieval Augmented Generation) com execução de código Python para análises dinâmicas.

> *"Qual foi o produto com maior crescimento no Q3 comparado ao Q2?"*  
> *"Quais clientes têm risco alto de churn nos próximos 30 dias?"*

## 🖥️ Demo

🔗 **[Acesse o demo ao vivo →](https://gabriel-rag-agent.streamlit.app)**

## 🏗️ Como Funciona

```
Arquivo (PDF/CSV/Excel)
    └─► Chunking + Embedding (text-embedding-3-small)
            └─► Pinecone Vector Store
                    └─► LangChain RetrievalQA
                            └─► GPT-4o (resposta + código)
                                    └─► Execução Python (pandas)
                                            └─► Resposta + Gráfico
```

## 🛠️ Stack

| Componente | Tech |
|-----------|------|
| LLM | OpenAI GPT-4o |
| Orquestração | LangChain 0.2 |
| Vector Store | Pinecone |
| Embeddings | text-embedding-3-small |
| API | FastAPI + Pydantic v2 |
| Interface | Streamlit |
| Deploy | Docker + Streamlit Cloud |

## 🚀 Rodando

```bash
git clone https://github.com/Kaique-ML/rag-analytics-agent
cd rag-analytics-agent

cp .env.example .env
# Configure: OPENAI_API_KEY, PINECONE_API_KEY, PINECONE_INDEX

docker compose up --build
# Acesse: http://localhost:8501
```

```bash
# Sem Docker
pip install -r requirements.txt
python scripts/ingest.py --file data/sample_sales.csv
streamlit run app/main.py
```

## 📂 Estrutura

```
rag-analytics-agent/
├── app/
│   ├── main.py                 # Streamlit UI
│   ├── agent/
│   │   ├── rag_chain.py        # LangChain RetrievalQA
│   │   └── code_executor.py    # Execução segura de Python
│   └── api/
│       └── routes.py           # FastAPI endpoints
├── scripts/
│   └── ingest.py               # Indexação de documentos
├── data/
│   └── sample_sales.csv        # Dataset de exemplo
├── tests/
│   └── test_agent.py
├── docker-compose.yml
└── .env.example
```

## 💬 Exemplos de Perguntas

```
✅ "Qual a receita total do último trimestre?"
✅ "Mostre um gráfico de vendas por região"
✅ "Quais produtos tiveram queda de mais de 20% em vendas?"
✅ "Compare o desempenho dos últimos 3 meses"
✅ "Quem são os top 5 clientes por LTV?"
```

## 📈 Métricas

- 🎯 **91% de precisão** nas respostas (avaliação manual, 100 perguntas)
- ⚡ **2.1s** de latência média por consulta
- 📄 Suporta arquivos de até **500 páginas**

---
**Gabriel Kaique Portel Silva** | [LinkedIn](https://linkedin.com/in/gabriel-kaique-881475284) | [GitHub](https://github.com/Kaique-ML)
