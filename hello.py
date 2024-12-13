import streamlit as st

st.header('st.button')

st.button('Reset', type='primary')

if st.button('Say hello'):      # 버튼을 누르면...
     st.write('Say Hello 버튼을 눌렀음..')
else:
     st.write('아무 선택도 없음.')


# 버튼을 3개 나열...
left, middle, right = st.columns(3)
if left.button("Plain button", use_container_width=True):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", use_container_width=True):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", use_container_width=True):
    right.markdown("You clicked the Material button.")