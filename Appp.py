import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import plotly.express as ps
import matplotlib.pyplot as plt
train=pd.read_excel(r'C:\Users\TARUN\Desktop\New folder (3)\BQ-Assignment-Data-Analytics.xlsx')
f=train.groupby('Item Sort Order')

t=pd.DataFrame(columns=['Item','Item Sort Order','Jan 20','Feb 20','March 20','Apr 20','May 20'])
item=[]
item_sort_order=[]
item_type=[]
for i in f['Item'].unique():
    item.append(*i)
for i in f['Item Sort Order'].unique():
    item_sort_order.append(*i)
for i in f['Item Type'].unique():
    item_type.append(*i)
t['Item']=item
t['Item Sort Order']=item_sort_order
t['Item Type']=item_type
l=[]
l1=[]
l2=[]
l3=[]
l4=[]
for i in train['Item'].unique():
    l.append(*train[(train.Date=='2020-01-01')&(train.Item==str(i))]['Sales'].values)
    l1.append(*train[(train.Date == '2020-02-01') & (train.Item == str(i))]['Sales'].values)
    l2.append(*train[(train.Date == '2020-03-01') & (train.Item == str(i))]['Sales'].values)
    l3.append(*train[(train.Date == '2020-04-01') & (train.Item == str(i))]['Sales'].values)
    l4.append(*train[(train.Date == '2020-05-01') & (train.Item == str(i))]['Sales'].values)
t['Jan 20']=l
t['Feb 20']=l1
t['March 20']=l2
t['Apr 20']=l3
t['May 20']=l4


st.title('Business Quant')
st.markdown('How you doin??')
data=t

st.sidebar.title('Item Type')


random_data=st.sidebar.radio("What's your type?",('Select All','Fruit','Vegetable'))
if(random_data=='Select All'):
    st.write(data)

else:
    modified_data = data[data['Item Type'] == random_data]
    st.write(modified_data)
select=st.sidebar.selectbox("What month's sale do you wanna know?",('Jan 20','Feb 20','March 20','Apr 20','May 20'))
m=['Jan 20','Feb 20','March 20','Apr 20','May 20']
for i in m:
    if(select==i):
        fig = ps.bar(t, t['Item'], t[str(i)])
        st.plotly_chart(fig)
