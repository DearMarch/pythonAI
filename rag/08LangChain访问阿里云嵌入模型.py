from langchain_community.embeddings import DashScopeEmbeddings

# 创建阿里云嵌入模型实例，使用默认配置初始化 DashScope 嵌入模型
model = DashScopeEmbeddings()

print(model.embed_query("我喜欢你"))
print(model.embed_documents(["我喜欢你", "我稀饭你", "晚上吃啥"]))
