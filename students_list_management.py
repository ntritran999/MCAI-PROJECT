import streamlit as st
import pandas as pd


def show_table():    
    
    def gender_filter(option,gender):
        if not option:
            df.drop(df[df['GENDER']==gender].index,inplace=True)   
            
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
    
    def period_filter():
        if len(session_option) == 1:
            if session_option[0] =='Sáng':
                return df[df['PYTHON-CLASS'].str.contains('S')]
            elif session_option[0] == 'Chiều':
                return df[df['PYTHON-CLASS'].str.contains('C')]
        elif len(session_option) == 2:
            return df 
    def specialized_class():
        if not literature:
            df.drop(df[df['CLASS'].str.contains('CV')].index,inplace=True)   
        if not math:
            df.drop(df[df['CLASS'].str.contains('CT1|CT2|CT3')].index,inplace=True)               
        if not physics:
            df.drop(df[df['CLASS'].str.contains('CL')].index,inplace=True)   
        if not chemistry:
            df.drop(df[df['CLASS'].str.contains('CH')].index,inplace=True)   
        if not english:
            df.drop(df[df['CLASS'].str.contains('CA')].index,inplace=True)   
        if not IT:
            df.drop(df[df['CLASS'].str.contains('CTIN')].index,inplace=True)           
        if not hstry_geo:
            df.drop(df[df['CLASS'].str.contains('CSD')].index,inplace=True)   
        if not t_n:
            df.drop(df[df['CLASS'].str.contains('CTRN')].index,inplace=True)   
        if not th_sn:
            df.drop(df[df['CLASS'].str.contains('TH|SN')].index,inplace=True)   
        if not others:
            df.drop(df[~df['CLASS'].str.contains('CV|CT|CL|CH|CA|CTIN|CSD|CTRN|TH|SN')].index,inplace=True)   


    df = pd.read_csv("py4ai-score.csv")
    df.fillna(0,inplace=True)
    df["REG-MC4AI"] = df["REG-MC4AI"].replace(0,"N")

    with st.container():    
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.write('Giới tính')
            check_male = st.checkbox('Nam',value=True)
            check_female = st.checkbox('Nữ',value=True)
            
                    

        with col2:
            class_option = st.radio('Khối lớp',('Tất cả','Lớp 10', 'Lớp 11', 'Lớp 12'))
            
            
        with col3:
            room_option = st.selectbox('Phòng',('Tất cả','A114','A115'))
            

        with col4:
            session_option = st.multiselect('Buổi',['Sáng','Chiều'])
            
    with st.container():
        st.write("Lớp chuyên")
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            literature = st.checkbox("Văn",value=True)
            math = st.checkbox("Toán",value=True)
    
        with col2:
            physics = st.checkbox("Lý",value=True)
            chemistry = st.checkbox("Hóa",value=True)   
    
        with col3:
            english = st.checkbox("Anh",value=True)
            IT = st.checkbox("Tin",value=True)
    
        with col4:
            hstry_geo = st.checkbox("Sử Địa",value=True)
            t_n = st.checkbox("Trung Nhật",value=True)
    
        with col5:
            th_sn = st.checkbox("TH/SN",value=True)
            others = st.checkbox("Khác",value=True)
            
    df = class_filter()
    df = room_filter()
    df = period_filter()
    if df is not None:
    	gender_filter(check_female,'F')
    	gender_filter(check_male,'M')

    	specialized_class()
    	if not df.empty:
    		df.reset_index(drop=True,inplace=True)
    		st.write('SỐ HỌC SINH : ',len(df.index), df['GENDER'].value_counts())	
    		st.write('GPA cao nhất: ', df['GPA'].max())
    		st.write('-'*6,'thấp nhất: ', df['GPA'].min())
    		st.write('-'*6,'trung bình: ', df['GPA'].mean().round(1))
    		st.dataframe(df)

