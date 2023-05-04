import streamlit as st
from students_list_management import show_table
from graphs import plot_student,plot_score

def main():
    st.header("BẢNG ĐIỂM LỚP PY4AI")


    tab1, tab2, tab3, tab4 = st.tabs(["Danh sách", "Biểu đồ", "Phân nhóm", "Phân loại"])

    with tab1:
        show_table()
    with tab2:
    	subtab1, subtab2 = st.tabs(['Số học sinh','Điểm'])
    	with subtab1:
    		plot_student()
    	with subtab2:
    		list_of_sessions = ('S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','GPA')
    		session = st.radio('session_selection',list_of_sessions,horizontal=True,label_visibility='hidden')
    		plot_score(session,list_of_sessions)
    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

if __name__=="__main__":
    main()

