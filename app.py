import streamlit as st
import pandas as pd

# 创建一个Streamlit侧边栏
st.sidebar.title("英语单词学习应用")

# 在侧边栏中添加一个文本输入框，用于输入新单词
new_word = st.sidebar.text_input("输入新单词:")

# 加载或创建一个存储单词的数据框
if 'vocab' not in st.session_state:
    st.session_state.vocab = pd.DataFrame(columns=['单词', '释义'])

# 检查是否输入了新单词
if new_word:
    new_definition = st.sidebar.text_input("输入释义:")
    if new_definition:
        st.session_state.vocab = st.session_state.vocab.append({'单词': new_word, '释义': new_definition}, ignore_index=True)

# 在主界面中显示当前的单词列表
st.title("当前的单词列表:")
st.dataframe(st.session_state.vocab)

# 在主界面中添加一个文本框，用于练习已有的单词
word_to_practice = st.text_input("输入要练习的单词:")

# 在主界面中添加一个按钮，用于检查单词的释义
if st.button("检查释义"):
    word_definition = st.session_state.vocab[st.session_state.vocab['单词'] == word_to_practice]['释义'].values
    if len(word_definition) > 0:
        st.write(f"单词 '{word_to_practice}' 的释义是: {word_definition[0]}")
    else:
        st.write("未找到该单词的释义。")

# 在主界面中添加一个按钮，用于清空单词列表
if st.button("清空单词列表"):
    st.session_state.vocab = pd.DataFrame(columns=['单词', '释义'])
    st.write("单词列表已清空。")
