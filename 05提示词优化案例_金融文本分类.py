from openai import OpenAI

# 1. 获取client对象，openai 类对象
client = OpenAI (
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

examples_data = {
    "新闻报道": "今日，股市经历了一轮震荡，受到经济危机的影响。投资者们开始考虑投资。",
    "财务报告": "本公司年度财务报告显示，去年公司的收入为10亿，利润为5亿。",
    "公司公告": "本公司高兴的宣布完成了一个新的项目，项目预计可以获得10万奖金。",
    "分析师报告": "最新的行业分析显示，科技领域的创新在中国有非常大的机会。"
}

examples_types = [
    "新闻报道",
    "财务报告",
    "公司公告",
    "分析师报告",
]

questions = [
    "今日，央行发布公告宣布降低存款利率， 以刺激经济增长",
    "ANC公司今日发布公告称，已完成一个新的项目，项目预计可以获得10万奖金。",
    "公司资产负债显示，公司偿债能力强劲，现金流充足。",
    "最新的分析报告指出，可再生资源的利用潜力非常高，可以产生非常大的利润。",
    "小明喜欢喝咖啡，他每天喝2杯咖啡。"
]

messages = [{
    "role": "system",
    "content": "你是一个金融专家，将文本分类为['新闻报道'， ‘财务报告'， ‘公司公告'， ‘分析师报告']，不清楚的分类为'其他'。"
}]

for key,value in examples_data.items():
    messages.append( {"role": "user", "content": value})
    messages.append( {"role": "assistant", "content": key})

for q in questions:
    response = client.chat.completions.create(
        model="qwen3.5-plus",
        messages=messages + [{"role": "user", "content": f"按照示例提示，回答这段文本的分类：{q}]"}],
    )
    print(response.choices[0].message.content)