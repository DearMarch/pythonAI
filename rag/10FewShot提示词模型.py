from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

# 创建示例
example_template = PromptTemplate.from_template("单词：{word}, 反义词：{antonym}")

# 创建 few-shot 示例
example_data = [
    {"word": "大", "antonym": "小"},
    {"word": "上", "antonym": "下"}
]

few_shot_prompt = FewShotPromptTemplate(
    example_prompt=example_template, # 示例模板
    examples=example_data,           # 示例数据
    prefix="告知我单词的反义词，我提供如下示例：",  # 示例之前的提示词
    suffix="基于前面的实力告知无单词：{input_word}的反义词：",  # 示例之后的提示词
    input_variables=["input_word"]             # 输入变量
)

prompt_text = few_shot_prompt.invoke(input = {"input_word": "左"}).to_string()
print(prompt_text)

model = Tongyi(model = "qwen-max")
res = model.invoke(input=prompt_text)
print(res)