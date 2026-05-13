from dashscope.models import Models

result = Models.list(page=1, page_size=50)
print(result.output)

for model in result.output['models']:
    print(model)
