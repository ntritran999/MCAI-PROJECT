import streamlit as st
import plotly.express as px
import pandas as pd
from sklearn.cluster import KMeans


df = pd.read_csv('py4ai-score.csv')
df.fillna(0,inplace=True)


start_column = df.columns.get_loc('S1')
end_column = df.columns.get_loc('S10')+1
df['S-AVG'] = df.iloc[:,start_column:end_column].mean(axis=1)


def draw_classification(n):
	wanted_session = ['S6','S10','S-AVG']
	session1,session2,session3 = wanted_session
	    
	kmeans = KMeans(n_clusters=n,n_init='auto')
	kmeans.fit(df[wanted_session].to_numpy())
	
	df['cluster'] = list(map(str,kmeans.labels_))
	st.plotly_chart(px.scatter_3d(df,x=session1,y=session2,z=session3,color='cluster'))
	
	for i in range(n):
		sub_df = df[df['cluster']==str(i)][['NAME','CLASS','GPA']]
		max_gpa,min_gpa,avg_gpa = sub_df['GPA'].max(), sub_df['GPA'].min(), sub_df['GPA'].mean().round(2)
		st.write(f'Nhóm {i+1}:','GPA cao nhất',max_gpa,',thấp nhất',min_gpa,',trung bình',avg_gpa)
		st.write(sub_df)

