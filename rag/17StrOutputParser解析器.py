from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
model = ChatTongyi(model="qwen3-max-2026-01-23")
prompt = PromptTemplate.from_template("他姓{lastname}，生了个{gender}，请起个名字，简单回答，仅起名，不回复其他")

chain = prompt | model | parser | model | parser
res: str = chain.invoke({"lastname": "王", "gender": "男"})
print(res)
print(type(res))