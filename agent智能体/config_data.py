
md5_path = "./md5.text"

# Chroma
collection_name = "rag"
persist_directory = "./chroma_db"

# TextSplitter
chunk_size = 1000
chunk_overlap = 100
separators = [",", "。", "；", "；", "？", "！", "，", "。", "；", "；", "？", "！"]
max_split_char_number = 1000


#
similarity_threshold = 2    # 相似度阈值

embedding_model_name = "text-embedding-v4"
chat_model_qwen = "qwen3.6-max-preview"
chat_model_deepseek = "deepseek-v4-flash"


session_config = {
        "configurable":{
            "session_id": "user_001"
        }
    }