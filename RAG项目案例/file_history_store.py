import os, json
from typing import Sequence

from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage


# 通过会话id获取InMemoryChatMessageHistory类对象
def get_history(session_id):

    return FileChatMessageHistory(session_id, "./chat_history")

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


