from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader(
    file_path="./data/Python基础语法.txt",
    encoding="utf-8"
)

docx = loader.load()


splitter = text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,     # 分段长度
    chunk_overlap=100,   # 分段重叠长度
    # 文本分段分隔符
    separators=["\n\n", "\n", "。", "！", "？", "；", "，", "、", "：", "（", "）", "【", "】", "《", "》", ],
    length_function=len    # 统计字符的依据函数
)
split_docs = splitter.split_documents(docx)
print(len(split_docs))

for split_doc in split_docs:
    print("="*20)
    print(split_doc)
    print("=" * 20)
