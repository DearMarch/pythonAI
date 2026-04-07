from dashscope.io import input_output
from langchain_community.chat_models import ChatTongyi
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.vectorstores import InMemoryVectorStore
from openai.types import vector_store
from rich import prompt
from torch.ao.nn.quantized import reference

model = ChatTongyi(model="qwen3-max-2026-01-23")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "以我提供的一直参考资料为主，简洁和专业的回答用户问题。参考资料：{context}"),
        ("user", "用户提问：{input}"),
    ]
)

vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings(model="text-embedding-v4"))

vector_store.add_texts(["减肥就是少吃多练", "在减脂期间吃东西很重要，清淡少油控制卡路里摄入并运动起来", "跑步是很好的运动哦"])

input_text = "怎么减肥？"

result = vector_store.similarity_search(input_text, k=2)
reference_text = "["
for doc in result:
    reference_text += doc.page_content
reference_text += "]"

def print_prompt(inputs):
    print("="*20, inputs.to_string(), "="*20)
    return inputs

chain = prompt | print_prompt | model | StrOutputParser()
res = chain.invoke({"input": input_text, "context": reference_text})
print(res)