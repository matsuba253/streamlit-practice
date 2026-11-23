
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="課題管理アプリ",
    page_icon="📚",
    layout="centered"
)

# デザイン設定
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f5f0ff, #eef4ff);
    color: #30264a;
}

div[data-testid="stAlert"] {
    background-color: white !important;
    border-radius: 12px;
}

div[data-testid="stAlert"] p {
    color: #30264a !important;
}

h1 {
    text-align: center;
    padding: 20px;
}

.subtitle {
    text-align: center;
    color: #776b91;
    margin-bottom: 30px;
}

div.stButton > button {
    background-color: #8064c8;
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #684bb0;
    color: white;
}

div[data-testid="stMetric"] {
    background-color: white;
    padding: 18px;
    border-radius: 15px;
    box-shadow: 0 3px 10px #d9d0eb;
}

/* 警告メッセージを白くする */
div[data-testid="stAlert"],
div[data-testid="stAlert"] > div {
    background: white !important;
    background-color: white !important;
}

div[data-testid="stAlert"] p,
div[data-testid="stAlert"] span {
    color: #30264a !important;
}

</style>
""", unsafe_allow_html=True)

st.title("📚 課題管理アプリ")
st.markdown(
    '<p class="subtitle">課題の締切と進捗を管理しよう</p>',
    unsafe_allow_html=True
)

if "tasks" not in st.session_state:
    st.session_state.tasks = []

# 課題の追加
st.subheader("✏️ 課題を追加")

task = st.text_input("課題名", placeholder="例：数学のレポート")
deadline = st.date_input("締切日")

if st.button("＋ 課題を追加", use_container_width=True):
    if task.strip():
        st.session_state.tasks.append({
            "name": task,
            "deadline": deadline,
            "done": False
        })
        st.success("課題を追加しました")
        st.rerun()
    else:
        st.warning("課題名を入力してください")

st.divider()

# 課題一覧
st.subheader("📋 課題一覧")

if len(st.session_state.tasks) == 0:
    st.info("まだ課題が登録されていません")

for i, t in enumerate(st.session_state.tasks):
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown(f"### 📖 {t['name']}")
            st.caption(f"締切日：{t['deadline']}")

        with col2:
            t["done"] = st.checkbox(
                "完了",
                value=t["done"],
                key=f"task_{i}"
            )

        remaining = (t["deadline"] - date.today()).days

        if t["done"]:
            st.success("🎉 完了！")
        elif remaining > 0:
            st.info(f"⏰ 締切まであと {remaining} 日")
        elif remaining == 0:
            st.warning("⚠️ 本日締切")
        else:
            st.error(f"🚨 締切から {-remaining} 日過ぎています")

st.divider()

# 進捗状況
st.subheader("📊 進捗状況")

total = len(st.session_state.tasks)
completed = sum(t["done"] for t in st.session_state.tasks)

if total > 0:
    progress = completed / total

    col1, col2 = st.columns(2)
    col1.metric("登録した課題", f"{total} 件")
    col2.metric("完了した課題", f"{completed} 件")

    st.progress(progress)
    st.markdown(f"### 進捗率：{progress * 100:.0f}%")
else:
    st.info("課題を追加すると進捗が表示されます")

