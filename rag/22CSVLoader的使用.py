from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="./data/stu.csv",
    encoding="utf-8",
    csv_args={
        "delimiter": ",",   # 分隔符
        "quotechar": "'"    # 指定带有分割符文本的引号包围的是单引号还是双引号
    }
)
# docs = loader.load()
# print(docs)
# for doc in loader.load():
#     print(type(doc), doc)

# 懒加载
for doc in loader.lazy_load():
    print(doc)