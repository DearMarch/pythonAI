from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser

str_parser = StrOutputParser()
json_parser = JsonOutputParser()
model = ChatTongyi(model="qwen3-max-2026-01-23")

first_prompt = PromptTemplate.from_template(
    "他姓{lastname}，生了个{gender}，请起个名字，请按照JSON格式返回：key为name，value为生成的名字，严格按照格式返回")


second_promt = PromptTemplate.from_template(
    "姓名：{name},解释下含义")


chain = first_prompt | model | json_parser | second_promt | model | str_parser
for chunk in chain.stream({"lastname": "赵", "gender": "男"}):
    print(chunk,end="", flush=True)
