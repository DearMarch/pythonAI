from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.runnables import RunnableLambda

str_parser = StrOutputParser()
model = ChatTongyi(model="qwen3-max-2026-01-23")

my_func = RunnableLambda(lambda ai_msg: {"name": ai_msg.content})

first_prompt = PromptTemplate.from_template(
    "他姓{lastname}，生了个{gender}，请起个名字，仅告知我名字，不要额外信息")


second_promt = PromptTemplate.from_template(
    "姓名：{name},解释下含义")


chain = first_prompt | model | my_func | second_promt | model | str_parser
for chunk in chain.stream({"lastname": "赵", "gender": "男"}):
    print(chunk,end="", flush=True)
