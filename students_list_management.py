import streamlit as st
import pandas as pd


def show_table():    
    
    def gender_filter(option,gender):
        if not option:
            df.drop(df[df['GENDER']==gender].index,inplace=True)   
            df.reset_index(drop=True,inplace=True)
    
    def class_filter(): 
        for class_num in ['10','11','12']:
            if class_option == ('Lớp ' + class_num):
                return df[df['CLASS'].str.contains(class_num)]
        return df    
    
    def room_filter(): 
        for room_name in ['A114','A115']:
            if room_option == (room_name):
                return df[df['PYTHON-CLASS'].str.contains(room_name[1:])]
        return df    
    def session_filter():
        if len(session_option) == 1:
            if session_option[0] =='Sáng':
                return df[df['PYTHON-CLASS'].str.contains('S')]
            elif session_option[0] == 'Chiều':
                return df[df['PYTHON-CLASS'].str.contains('C')]
        elif len(session_option) == 2:
            return df 

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
            class_option = st.radio('Khối lớp',('Tất cả','Lớp 10', 'Lớp 11', 'Lớp 12'))
            df = class_filter()
            
        with col3:
            room_option = st.selectbox('Phòng',('Tất cả','A114','A115'))
            df = room_filter()

        with col4:
            session_option = st.multiselect('Buổi',['Sáng','Chiều'])
            df = session_filter()
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

    if df is not None and not df.empty:
    	df.reset_index(drop=True,inplace=True)
    	students_count = len(df.index)
    	st.write('Số học sinh: ',students_count, df['GENDER'].value_counts())	
    	st.write('GPA cao nhất: ', df['GPA'].max())
    	st.write('-'*6,'thấp nhất: ', df['GPA'].min())
    	st.write('-'*6,'trung bình: ', df['GPA'].mean().round(1))
    	st.dataframe(df)

