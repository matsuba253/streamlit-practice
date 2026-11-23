import streamlit as st
from datetime import date

st.title("課題管理アプリ")
st.write("課題の締切を管理しよう！")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

task = st.text_input("課題名")
deadline = st.date_input("締切日")

if st.button("追加"):
    if task:
        st.session_state.tasks.append({
            "name": task,
            "deadline": deadline
        })

st.subheader("課題一覧")

for i, t in enumerate(st.session_state.tasks):
    st.write(
        f"{t['name']} / 締切：{t['deadline']}"
    )
    st.checkbox("完了", key=f"task_{i}")

