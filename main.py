import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35,139],
    columns=['lat','lon']
)

#st.line_chart(df)

#st.dataframe(df.style.highlight_max(axis=0))

st.map(df)

st.write('Interactive Widgets')

text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味：', text

condition = st.slider('あなたの今の調子は？',0,100,50)
'あなたの調子：', condition



"""
# 章
## 節
### 項
"""


