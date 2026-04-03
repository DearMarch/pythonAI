"""
基于 LangChain 的内存向量存储示例

该模块演示了如何使用 InMemoryVectorStore 进行文档的向量化存储和相似度搜索。
主要功能包括：
- 加载 CSV 格式的文档数据
- 使用通义千问嵌入模型生成向量
- 将文档存储到内存向量数据库中
- 执行相似度搜索查询
"""
from langchain_community.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

# 初始化内存向量存储，使用通义千问嵌入模型
vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings())


# 配置 CSV 文档加载器，指定文件路径、编码格式和来源列
loader = CSVLoader(
    file_path="./data/info.csv",
    encoding="utf-8",
    source_column="source"
)

# 加载 CSV 文件中的所有文档
docs = loader.load()

# 将文档添加到向量存储中，并为每个文档生成唯一 ID
vector_store.add_documents(
    documents=docs,
    ids=["id"+str(i) for i in range(1,len(docs)+1)]
)

# 从向量存储中删除指定 ID 的文档
vector_store.delete(["id1","id2"])

# 执行相似度搜索，查找与"AI 学习"最相关的 2 个文档
result = vector_store.similarity_search("AI 学习", k=2)
print(result)
