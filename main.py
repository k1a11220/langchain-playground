from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import TextLoader

loader = UnstructuredPDFLoader("test.pdf")
docs = loader.load()

print(docs[0].page_content[0:100])