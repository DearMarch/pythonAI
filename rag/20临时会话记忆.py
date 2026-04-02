from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model = ChatTongyi(model="qwen3-max-2026-01-23")
# prompt = PromptTemplate.from_template(
#     "你需要根据会话历史回答用户问题。对话历史：{chat_history}，用户提问：{input}，请回答")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你需要根据会话历史回答用户问.对话历史"),
        MessagesPlaceholder("chat_history"),
        ("human", "请回答如下问题：{input}"),
    ]
)

str_parser = StrOutputParser()

def print_prompt(inputs):
    print("="*20, inputs.to_string(), "="*20)
    return inputs

base_chain = prompt | print_prompt | model | str_parser

store = {} # key是session_id -> value是InMemoryChatMessageHistory类对象

# 通过会话id获取InMemoryChatMessageHistory类对象
def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 创建一个新的链，对原有链进行增强，自动附加历史消息
history_chain = RunnableWithMessageHistory(
    base_chain,         # 基础链
    get_history,        # 通过会话id获取InMemoryChatMessageHistory类对象
    message_key="chat_history",
    input_messages_key="input",
    history_messages_key="chat_history"
)

if __name__ == '__main__':
    # 固定格式，添加langchain配置，为当前程序配置所属的session_id
    session_config = {
        "configurable":{
            "session_id": "user_001"
        }
    }
    res = history_chain.invoke({"input": "小明有两只猫"}, session_config)
    print("第一次执行：", res)
    res = history_chain.invoke({"input": "小红有一只狗"}, session_config)
    print("第二次执行：", res)
    res = history_chain.invoke({"input": "总共有几只宠物"}, session_config)
    print("第三次执行：", res)