import streamlit as st
import time

from rag import RagService
import config_data as config

# 标题
st.title("智能客服")
st.divider()

if "rag" not in st.session_state:
    st.session_state["rag"] = RagService()

if "message" not in st.session_state:
    st.session_state["message"] = [{"role": "assistant", "content": "你好，欢迎来到智能客服系统"}]

for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])

# 在页面最下方提供用户输入框
prompt = st.chat_input()

if prompt:
    # 用户输入框有内容时，将用户输入框内容显示在页面
    st.chat_message("user").write(prompt)
    st.session_state["message"].append({"role": "user", "content": prompt})
    ai_res_list = []
    with st.spinner("AI思考中："):
        res_stream = st.session_state["rag"].chain.stream({"input": prompt}, config.session_config)

        def capture(generator, cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                yield chunk

        st.chat_message("assistant").write_stream(capture(res_stream, ai_res_list))
        st.session_state["message"].append({"role": "assistant", "content": "".join(ai_res_list)})