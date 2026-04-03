from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader(
    file_path="./data/Python基础语法.pdf",
    mode="single"                   # 默认为"page"
)


docs = loader.lazy_load()

i = 0
for doc in loader.lazy_load():
    i += 1
    print(doc)
    print("="*20, i)