import streamlit as st

st.title("Hello, Streamlit!")
st.write("これは最小構成のStreamlitアプリです。")



import streamlit as st
import json
from pathlib import Path


# JSONファイルを読み込む
json_file_path = Path(__file__).parent / "sample_data" / "highlow.json"

with open(json_file_path, "r" , encoding="utf-8") as f:
    data = json.load(f)

#　カードの情報
base_card = data["base_card"]
result_card = data["result_card"]

#　タイトル
st.title("High & Low")
st.write("次のカードは大きい？　小さい？")

#　最初のカードを表示
st.write("最初のカード")
st.header(
    f"{base_card['suit']}{base_card['rank']}"
)

#　次のカードを表示
st.write("次のカード")
st.header(
    f"{result_card['suit']}{result_card['rank']}"
)
