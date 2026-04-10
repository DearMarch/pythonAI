import streamlit as st

# 设置应用标题
st.title("知识库更新服务")

# 创建文件上传组件,仅接受TXT格式文件
uploader_file = st.file_uploader(
    "请上传TXT文件",
    type=['txt'],
    accept_multiple_files=False,
)

# 处理用户上传的文件:解析文件信息并显示内容
if uploader_file is not None:
    file_name = uploader_file.name
    file_type = uploader_file.type
    file_size = uploader_file.size / 1024

    st.subheader(f"文件名:{file_name}")
    st.write(f"格式:{file_type} | 大小: {file_size: .2f} KB")

    # 读取文件内容并以UTF-8编码解码显示
    text = uploader_file.getvalue().decode("utf-8")
    st.write(text)
