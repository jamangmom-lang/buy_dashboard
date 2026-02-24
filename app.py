import streamlit as st
import pandas as pd

st.title("구매팀 대시보드 (초안)")

uploaded = st.file_uploader("엑셀 파일 업로드", type=["xlsx", "xls"])

# ✅ 업로드 파일을 세션에 저장
if uploaded is not None:
    st.session_state["uploaded_bytes"] = uploaded.getvalue()

if "uploaded_bytes" in st.session_state:
    data = st.session_state["uploaded_bytes"]

    preview = pd.read_excel(data, header=None)
    st.success("엑셀 로딩 완료! (헤더 줄 선택 필요)")
    st.dataframe(preview.head(20))

    header_row = st.number_input(
        "헤더(컬럼명)로 사용할 행 번호 선택 (0부터 시작)",
        min_value=0,
        max_value=int(min(50, len(preview)-1)),
        value=0,
        step=1
    )

    df = pd.read_excel(data, header=int(header_row))

    st.subheader("정리된 데이터")
    st.dataframe(df)

    if st.button("업로드 초기화"):
        st.session_state.pop("uploaded_bytes", None)
        st.rerun()
else:
    st.info("엑셀 파일을 업로드하면 표가 보입니다.")
