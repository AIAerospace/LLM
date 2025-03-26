# Importar dependencias
import os
import openai
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

openai.api_key = os.getenv("OPENAI_API_KEY")

print("Cargando modelo de lenguaje...")