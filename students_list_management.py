import streamlit as st
import pandas as pd


def show_table():    
    def gender_filter(option,gender):
        if not option:
            df.drop(df[df['GENDER']==gender].index,inplace=True)   
            df.reset_index(drop=True,inplace=True)
    
    df = pd.read_csv("py4ai-score.csv")
    df.fillna(0,inplace=True)
    df["REG-MC4AI"] = df["REG-MC4AI"].replace(0,"N")

    with st.container():    
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.write('Giới tính')
            check_male = st.checkbox('Nam',value=True)
            check_female = st.checkbox('Nữ',value=True)
            gender_filter(check_male,'M')
            gender_filter(check_female,'F')        

        with col2:
            st.radio('Khối lớp',('Tất cả','Lớp 10', 'Lớp 11', 'Lớp 12'))

        with col3:
            st.selectbox('Phòng',('Tất cả','A114','A115'))

        with col4:
            st.multiselect('Buổi',['Sáng','Chiều'])

    with st.container():
        st.write("Lớp chuyên")
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            st.checkbox("Văn",value=True)
            st.checkbox("Toán",value=True)
    
        with col2:
            st.checkbox("Lý",value=True)
            st.checkbox("Hóa",value=True)   
    
        with col3:
            st.checkbox("Anh",value=True)
            st.checkbox("Tin",value=True)
    
        with col4:
            st.checkbox("Sử Địa",value=True)
            st.checkbox("Trung Nhật",value=True)
    
        with col5:
            st.checkbox("TH/SN",value=True)
            st.checkbox("Khác",value=True)


    st.dataframe(df)

