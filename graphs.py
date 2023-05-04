import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('py4ai-score.csv')
df['Số học sinh'] = [1 for i in range(len(df))]

for i in df.index:
	if 'M' in df['GENDER'][i]:
		df.loc[i, 'GENDER'] = 'Nam'
	if 'F' in df['GENDER'][i]:
		df.loc[i, 'GENDER'] = 'Nữ'

	if '114' in df['PYTHON-CLASS'][i]:
		df.loc[i, 'PYTHON-CLASS'] = 'Lớp 114'
	if '115' in df['PYTHON-CLASS'][i]:
		df.loc[i, 'PYTHON-CLASS'] = 'Lớp 115'

	if 'CV' in df['CLASS'][i]: 
		df.loc[i, 'CLASS'] = 'Chuyên Văn'
	elif 'CT1' in df['CLASS'][i] or 'CT2' in df['CLASS'][i] or 'CT3' in df['CLASS'][i]: 
		df.loc[i, 'CLASS'] = 'Chuyên Toán'
	elif 'CL' in df['CLASS'][i]: 
		df.loc[i, 'CLASS'] = 'Chuyên Lý'
	elif 'CH' in df['CLASS'][i]: 
		df.loc[i, 'CLASS'] = 'Chuyên Hóa'
	elif 'CA' in df['CLASS'][i]: 
		df.loc[i, 'CLASS'] = 'Chuyên Anh'
	elif 'CTIN' in df['CLASS'][i]: 
		df.loc[i, 'CLASS'] = 'Chuyên Tin'
	elif 'CSD' in df['CLASS'][i]: 
		df.loc[i, 'CLASS'] = 'Chuyên Sử-Địa'
	elif 'CTRN' in df['CLASS'][i]: 
		df.loc[i, 'CLASS'] = 'Chuyên Trung-Nhật'
	elif 'TH' in df['CLASS'][i] or 'SN' in df['CLASS'][i]: 
		df.loc[i, 'CLASS'] = 'TH/SN'
	else: 
		df.loc[i, 'CLASS'] = 'Khác'
				
def plot_student():
	for category in ['GENDER','CLASS','PYTHON-CLASS']:
		st.plotly_chart(px.pie(df,names=category,values='Số học sinh'))	
def plot_score(option,list_of_option):
	if option in list_of_option :
		st.plotly_chart(px.box(df,y=option,color='GENDER'))
		st.plotly_chart(px.box(df,y=option,x='CLASS',color='CLASS'))
		st.plotly_chart(px.box(df,y=option,x='CLASS',color='GENDER'))
