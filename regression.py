import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go	
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


df = pd.read_csv('py4ai-score.csv')
df.fillna(0,inplace=True)

start_column = df.columns.get_loc('S1')
end_column = df.columns.get_loc('S10')+1
df['S-AVG'] = df.iloc[:,start_column:end_column].mean(axis=1)


def draw_linear():
	x = df['S6'].to_numpy().reshape(-1,1)
	y = df['S-AVG'].to_numpy().reshape(-1,1)
	
	model = LinearRegression()
	model.fit(x,y)
	
	x_predict = df['S10'].to_numpy().reshape(-1,1)
	y_predict = model.predict(x_predict)
	
	df['Distance'] = y - y_predict
	

	fig,ax=plt.subplots()
	ax.scatter(x,y,c=np.where(df['Distance']>0,'r','g'))
	ax.plot(x_predict,y_predict)
	st.pyplot(fig)
	st.write(model.score(x,y).round(3))
def draw_multi_linear():
	X = df[['S6', 'S10']].values
	Y = df['S-AVG'].values
	
	multi_model = LinearRegression()
	multi_model.fit(X,Y)
	
	x=df['S6'].to_numpy()
	y=df['S10'].to_numpy()

	xx, yy = np.meshgrid(x,y)
	xy = np.c_[xx.ravel(), yy.ravel()]

	z= multi_model.predict(xy).reshape(xx.shape)


	fig = go.Figure(data=[go.Surface(x=x, y=y, z=z),go.Scatter3d(x=df['S6'],y=df['S10'],z=df['S-AVG'],mode='markers')])
	st.plotly_chart(fig)
	st.write(multi_model.score(X,Y))
