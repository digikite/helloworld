import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# 예제 1

st.write('Hello, *World!* :sunglasses:')  # 뒤는 아이콘
st.write('Hello, *World!*')

# 예제 2

st.write(1234)   # 문자가 아닌 숫자도 표시 가능

# 예제 3

df = pd.DataFrame({
     '첫 번째 컬럼': [1, 2, 3, 4],
     '두 번째 컬럼': [10, 20, 30, 40]
     })
st.write(df)

# 예제 4

st.write('아래는 DataFrame입니다.', df, '위는 dataframe입니다.')

# 예제 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),   # random.randn평균0, 표준편차1의 가우시안 표준정규분포 난수를 matrix array(m,n)생성
     columns=['a', 'b', 'c'])

c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)  # 변수로 전달 받아서 표시도 가능
