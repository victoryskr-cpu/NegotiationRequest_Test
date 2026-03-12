
import streamlit as st
from crawler_site_handlers import check_site
from data_targets import TARGET_SITES

st.set_page_config(page_title="NegotiationRequest Test", layout="wide")

st.title("지자체 교섭요구공고 테스트 크롤러")

if st.button("테스트 실행"):
    results = []
    for name, url in TARGET_SITES:
        result = check_site(name, url)
        results.append(result)

    st.write(results)
