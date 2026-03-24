from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import ChatPromptTemplate

template = PromptTemplate.from_template("名字是：{lastname}, 爱好：{hobby}")

# format(k1=v1, k2=v2...)
res = template.format(lastname = "haha", hobby="football")
print(res, type(res))

# invoke({"k1":v1, "k2":v2...})
res2 = template.invoke({"lastname": "kaka", "hobby":"baseball"})
print(res2, type(res2))