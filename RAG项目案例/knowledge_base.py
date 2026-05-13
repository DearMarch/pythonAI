"""
知识库
"""
import os
import config_data as config
import hashlib
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from datetime import datetime

def check_md5(md5_str: str):

    if not os.path.exists(config.md5_path):
        open(config.md5_path, "w", encoding="utf-8").close()
        return False
    else:
        for line in open(config.md5_path, "r", encoding="utf-8").readlines():
            line = line.strip()
            if line == md5_str:
                return True

        return False


def save_md5(md5_str: str):

    with open(config.md5_path, "a", encoding="utf-8") as f:
        f.write(md5_str + "\n")


def get_string_md5(input_str: str, encoding="utf-8"):
    str_bytes = input_str.encode(encoding=encoding)

    md5_obj = hashlib.md5()
    md5_obj.update(str_bytes)
    md5_hex = md5_obj.hexdigest()

    return md5_hex

class KnowledgeBaseService(object):
    def __init__(self):
        # 如果文件不存在则创建，存在则跳过
        os.makedirs(config.persist_directory, exist_ok=True)
        self.chroma = Chroma(
            collection_name=config.collection_name,   # 数据库表名
            embedding_function=DashScopeEmbeddings(model="text-embedding-v4"),
            persist_directory=config.persist_directory,   # 数据库本地存储文件路径
        )
        self.spliter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,    # 分割的块大小
            chunk_overlap=config.chunk_overlap,    # 块之间重叠的大小
            separators=config.separators,       # 文本分段分隔符
            length_function=len,
        )    # 文本分割的对象

    def update_by_str(self, data:str, filename):
        """将传入的字符串，进行向量化，存入向量数据库中"""
        # 获取md5
        md5_hex = get_string_md5(data)

        if check_md5(md5_hex):
            return "[跳过]内容已经存在知识库中"

        if len(data) > config.max_split_char_number:
            konwledge_chuns: list[str] = self.spliter.split_text(data)
        else:
            konwledge_chuns = [data]

        metadata = {
            "source": filename,
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operator": "pythonAI",
        }

        self.chroma.add_texts(
            texts=konwledge_chuns,
            metadatas=[metadata for _ in konwledge_chuns]
        )

        save_md5(md5_hex)

        return "[完成]向量数据库更新完成"


if __name__ == '__main__':
    service = KnowledgeBaseService()
    r = service.update_by_str("你好啊,明天", "testfile")
    print(r)