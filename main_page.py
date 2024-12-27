import streamlit as st

st.title('SK네트웍스 Family AI 캠프 9기')
st.header('오늘의 회식에 대해.ARABOJA')
st.subheader('장소 및 위치: 펀비어킹 금천 독산역점 18시')

menu_time = st.text_input('당신의 메뉴픽을 입력해주세요!')

if st.button(f'오늘의 메뉴를 간단히 입력해주세요'): # bool type
    st.write(menu_time)
    st.success(f'{menu_time} 먹고 달려보자!', icon='👍')

# 서브 페이지에 대한 디렉토리명은 무조건 pages로 해야 한다.

print('수정 사항 테스트')
