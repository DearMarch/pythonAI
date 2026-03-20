from openai import OpenAI

client = OpenAI (
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

examples_data = {
    "是": [
        ("公司ABC发布了季度财报，显示盈利增长。", "财报披露，公司ABC利润上升。"),
        ("公司ITCAST发布了年度财报，显示盈利大幅度增长。", "财报披露，公司ITCAST更赚钱了。")
    ],
    "不是":[
        ("黄金价格下跌，投资者抛售。", "外汇市场交易额创下新高。"),
        ("央行降息，刺激经济增长。", "新能源技术的创新。")
    ]
}

questions = [
    ("油价大幅下跌，能源公司面临挑战。", "未来新能源城市的建设趋势越加明显。"),
    ("股票市场今日大好，投资者乐观。", "持续上涨的市场让投资者感到满意。")
]

messages = [{
    "role": "system",
    "content": f"你帮我完成文本匹配，我给你2个句子，被[]包围，你判断它们是否匹配，回答是或不是，请参考如下示例："
}]

for key,value in examples_data.items():
    for t in value:
        messages.append({"role": "user", "content": f"句子1：[{t[0]}]，句子2：[{t[1]}]"})
        messages.append({"role": "assistant", "content": key})

for message in messages:
    print(message)

for q in questions:
    response = client.chat.completions.create(
        model="qwen3.5-plus",
        messages=messages + [{"role": "user", "content": f"句子1：[{q[0]}], 句子2：[{q[1]}]"}]
    )
    print(response.choices[0].message.content)
