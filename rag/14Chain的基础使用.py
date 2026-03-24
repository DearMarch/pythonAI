from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个边塞词人，可以写词。"),
        MessagesPlaceholder("history"),
        ("human", "请再写一首宋词")
    ]
)

history_data = [
    ("human", "你来写一首宋词"),
    ("ai",
     "醉里挑灯看剑，梦回吹角连营。八百里分麾下炙，五十弦翻塞外声。沙场秋点兵。马作的卢飞快，弓如霹雳弦惊。了却君王天下事，赢得生前身后名。可怜白发生！")
]

model = ChatTongyi(model="qwen3-max")

chain = prompt | model

# 通过链去调用invoke
# res = chain.invoke({"history": history_data})
# print(res.content, type(res))

# 通过链去调用stream
for chunk in chain.stream({"history": history_data}):
    print(chunk.content, end="", flush=True)
