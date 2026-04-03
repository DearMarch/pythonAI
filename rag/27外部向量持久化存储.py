from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

# 初始化 Chroma 向量存储，配置集合名称、嵌入函数和持久化目录
vector_store = Chroma(
    collection_name="test",
    embedding_function=DashScopeEmbeddings(),
    persist_directory="./chroma_db"
)


# # 使用 CSVLoader 加载文档数据，指定文件路径、编码和源列
# loader = CSVLoader(
#     file_path="./data/info.csv",
#     encoding="utf-8",
#     source_column="source"
# )
#
# docs = loader.load()
#
# # 将加载的文档添加到向量存储中，并为每个文档生成自定义 ID
# vector_store.add_documents(
#     documents=docs,
#     ids=["id"+str(i) for i in range(1,len(docs)+1)]
# )
#
# # 从向量存储中删除指定 ID 的文档
# vector_store.delete(["id1","id2"])

# 执行相似度搜索，查询与"AI 学习"最相似的 2 个文档
result = vector_store.similarity_search(
    "AI 学习",
    k=2,
    filter={"source": "机器学习算法"}
)
print(result)
