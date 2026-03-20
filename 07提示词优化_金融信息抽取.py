import json

from openai import OpenAI

client = OpenAI (
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

schema = {'日期', '股票名称','开盘价', '收盘价', '成交量'}

examples_data = [
  {
    "content": "2023-01-10，股市震荡，股票强大科技A股今日开盘价100人民币，一度飙升至105人民币，随后回落至98人民币，最终以102人民币收盘，成交量达到520000。",
    "answers": {
      "日期": "2023-01-10",
      "股票名称": "强大科技A股",
      "开盘价": "100人民币",
      "收盘价": "102人民币",
      "成交量": "520000"
    }
  },
  {
    "content": "2024-05-16，股市利好，股票英伟达美股今日开盘价105美元，一度飙升至109美元，随后回落至100美元，最终以116美元收盘，成交量达到3560000。",
    "answers": {
      "日期": "2024-05-16",
      "股票名称": "英伟达美股",
      "开盘价": "105美元",
      "收盘价": "116美元",
      "成交量": "3560000"
    }
  }
]

questions = [
  "2025-06-16，股市利好，股票伟岸新材A股今日开盘价66人民币，一度飙升至70人民币，随后回落至65人民币，最终以68人民币收盘，成交量达到123000。",
  "2025-06-06，股市利好，股票黑马程风A股今日开盘价200人民币，一度飙升至211人民币，随后回落至201人民币，最终以206人民币收盘。"
]

messages = [
  {
    "role": "system",
    "content": f"你是一个金融专家，帮我完成信息抽取，抽取{schema}信息，按Json字符串输出，如果某些信息不存在，用‘原文未提及’表示，请参考如下示例：。"
  }
]
for example in examples_data:
    messages.append({"role": "user", "content": example["content"]})
    messages.append({"role": "assistant", "content": json.dumps(example["answers"], ensure_ascii=False)})

for q in questions:
    response = client.chat.completions.create(
        model="qwen3.5-plus",
        messages=messages + [{"role": "user", "content": f"请根据文本，抽取信息：{q}"}]
    )
    print(response.choices[0].message.content)