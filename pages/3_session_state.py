import streamlit as st

st.title('회식 참여자 음주량 Checker')

# streamlit은 화면을 생성할 때마다 처음부터 코드를 렌더링하는 방식이다.
# 따라서 저장이 되지 않기 때문에 초기 설정을 아래와 같이 잡아주는 것이 좋다.
if 'drink_checker' not in st.session_state:
    st.session_state.drink_checker = 0

if st.button('누구던지 마실 때마다 누르기!'):
    st.session_state.drink_checker += 1

if st.button('정산하고 집가기'):
    st.session_state.drink_checker = 0

st.write(f'지금까지 마신 술병: {st.session_state.drink_checker}')
