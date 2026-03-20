from langchain_community.llms.tongyi import Tongyi


model = Tongyi(model="qwen-plus")

# 调用invoke向模型提问
res = model.invoke(input="你是谁？")

print(res)