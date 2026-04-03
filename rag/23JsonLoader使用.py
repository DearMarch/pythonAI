from langchain_community.document_loaders import JSONLoader

# loader = JSONLoader(
#     file_path="./data/stus.json",
#     jq_schema=".[].name",
#     text_content=False  # 告知JSONLoader类，数据源中的数据是结构化的数据，而不是字符串
# )

loader = JSONLoader(
    file_path="./data/stu_json_lines.json",
    jq_schema=".name",
    text_content=False,  # 告知JSONLoader类，数据源中的数据是结构化的数据，而不是字符串
    json_lines=True      # 告知JSONLoader类，数据源中的数据是JSONLines格式的
)

doc = loader.load()
print(doc)