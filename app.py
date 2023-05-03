import streamlit as st
from students_list_management import show_table
from graphs import plotting

def main():
    st.header("BẢNG ĐIỂM LỚP PY4AI")


    tab1, tab2, tab3, tab4 = st.tabs(["Danh sách", "Biểu đồ", "Phân nhóm", "Phân loại"])

    with tab1:
        show_table()
    with tab2:
    	plotting()
    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

if __name__=="__main__":
    main()

