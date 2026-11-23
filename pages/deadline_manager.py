
import streamlit as st
from datetime import date

st.title("📚 課題管理アプリ")
st.write("課題の締切と進捗状況を管理しよう！")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

# 課題の追加
st.subheader("課題を追加")

task = st.text_input("課題名")
deadline = st.date_input("締切日")

if st.button("課題を追加"):
    if task:
        st.session_state.tasks.append({
            "name": task,
            "deadline": deadline,
            "done": False
        })
        st.success("課題を追加したよ！")

# 課題一覧
st.subheader("📋 課題一覧")

for i, t in enumerate(st.session_state.tasks):
    st.write(f"**{t['name']}**")

    remaining = (t["deadline"] - date.today()).days

    if remaining > 0:
        st.info(f"締切まであと {remaining} 日！")
    elif remaining == 0:
        st.warning("今日が締切！！")
    else:
        st.error(f"締切から {-remaining} 日過ぎています")

    t["done"] = st.checkbox(
        "完了",
        value=t["done"],
        key=f"task_{i}"
    )

# 進捗状況
st.subheader("📊 進捗状況")

total = len(st.session_state.tasks)
completed = sum(t["done"] for t in st.session_state.tasks)

if total > 0:
    progress = completed / total

    st.write(f"完了した課題：{completed} / {total}")
    st.progress(progress)
    st.write(f"進捗率：{progress * 100:.0f}%")
else:
    st.write("まだ課題が登録されていません")



