import streamlit as st

st.title('회식 참가자 확인 하기')

col1, _, col2 = st.columns(3)

with col1:
    name = st.text_input('성함 입력')
    st.write(f'귀하의 성함을 확인해 주세요: {name}')

    age = st.number_input('연령 입력 (만 나이)', min_value=19, max_value=49)
    st.write(f'귀하의 연령을 확인해 주세요: {age}')

    options = ['남자', '여자', '감자']
    selected = st.selectbox('성별 입력', options) # 셀렉트 박스

    r_options1 = ['1차', '2차', '3차'] # 라디오 버튼
    choice = st.radio('어디까지 달리고 싶나요 ?', r_options1)

    r_options2 = ['한식', '중식', '일식', '양식', '분식']
    selected_many = st.multiselect('입맛 확인하기!', r_options2)

with _:
    pass

with col2:
    if st.checkbox('참가 확인'):
        st.write(f'성함: {name}')
        st.write(f'연령: {age}')
        st.write(f'성별: {selected}')
        st.write(f'오늘 몇 차 까지 ? {choice}')
        st.write(f'평소 입맛 {selected_many}')
        if st.button('제출하기'): # bool type
            st.success('확인했습니다❤️', icon='❤️')
