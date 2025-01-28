from langchain_community.document_loaders import UnstructuredPDFLoader
import nltk
# nltk.download('all')
# url1 = ""
# url2 = ""

# loader = WebBaseLoader(web_path=(url1, url2))
# loader = CSVLoader(file_path='propeller_simple.csv', encoding='utf-8')
pdf_filepath = 'test.pdf'
loader = UnstructuredPDFLoader(pdf_filepath)

docs = loader.load()

print(docs[0].page_content[0:100])