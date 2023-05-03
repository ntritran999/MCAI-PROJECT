import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('py4ai-score.csv')

for i in df.index:
	if 'CV' in df['CLASS'][i]: 
		df.loc[i, 'CLASS'] = 'Chuyên Văn'
	elif 'CT' in df['CLASS'][i]: 
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
		
		
def plotting():
	for category in ['GENDER','CLASS','PYTHON-CLASS']:
		st.plotly_chart(px.pie(df,names=category))	


