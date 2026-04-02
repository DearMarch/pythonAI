import os, json
from typing import Sequence

from langchain_community.chat_models import ChatTongyi
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory


# message_to_dict:  将message(BaseMessage类实例)对象转换成字典
# messages_from_dict:  将字典转换成message对象
# AIMessage、HumanMessage、SystemMessage 都是BaseMessage的子类


class FileChatMessageHistory(BaseChatMessageHistory):

    def __init__(self, session_id, storage_path):
        self.session_id = session_id    # 会话id
        self.storage_path = storage_path  # 存储路径
        # 完整的文件路径
        self.file_path = os.path.join(self.storage_path, self.session_id)

        # 确保文件夹是存在的
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        # Sequence实例 类似 list
        all_messages = list(self.messages)  # 已有的消息列表
        all_messages.extend(messages)       # 已有的消息列表 + 新的

        # 将数据同步写入本地文件中
        # 类对象写入文件-> 一堆二进制
        # 为了方便，可以将BaseMessage对象转换成字典(借助json模块以json字符串写入文件)
        # 官方 message_to_dict: 将单个message(BaseMessage类实例)对象转换成字典
        # new_messages = []
        # for message in all_messages:
        #     new_messages.append(message_to_dict(message))
        new_messages = [message_to_dict(message) for message in all_messages]
        # 将数据写入文件
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(new_messages, f)


    @property    # @property装饰器：将方法变为属性
    def messages(self) -> list[BaseMessage]:
        # 当前文件内： list[字典]
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                messages_data = json.load(f) # 返回值就是：list[字典]
                # 官方 messages_from_dict: 将字典转换成message对象
                return messages_from_dict(messages_data)
        except FileNotFoundError:
            return []

    def clear(self) -> None:
        # 删除文件
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([], f)


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

# 通过会话id获取InMemoryChatMessageHistory类对象
def get_history(session_id):

    return FileChatMessageHistory(session_id, "./chat_history")

# 创建一个新的链，对原有链进行增强，自动附加历史消息
history_chain = RunnableWithMessageHistory(
    base_chain,         # 基础链
    get_history,        # 通过会话id获取InMemoryChatMessageHistory类对象
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
    # res = history_chain.invoke({"input": "小明有两只猫"}, session_config)
    # print("第一次执行：", res)
    # res = history_chain.invoke({"input": "小红有一只狗"}, session_config)
    # print("第二次执行：", res)
    res = history_chain.invoke({"input": "总共有几只宠物"}, session_config)
    print("第三次执行：", res)

