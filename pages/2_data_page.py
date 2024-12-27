import streamlit as st
import pandas as pd

st.title('회식 참여자들의 Coding Level')

data = pd.DataFrame({
    'Coding Level': ['Lv.5', 'Lv.4', 'Lv.3', 'Lv.2', 'Lv.1'],
    'Level / People': [4, 8, 12, 4, 2],
    'Python Experience (%)': [79, 57, 43, 24, 4],
    'Other Language Experience (%)': [88, 62, 35, 11, 1]
})

# st.dataframe(data, use_container_width=True) # 데이터프레임을 보여만 주기

# edited_data = st.data_editor(data) # 데이터프레임을 수정도 가능하게 하기
# st.write(edited_data)

st.data_editor(data, use_container_width=True)

st.bar_chart(data.set_index('Coding Level')['Level / People'])
st.line_chart(data.set_index('Coding Level')['Python Experience (%)'])
fig  = data.plot.pie(
    y = 'Other Language Experience (%)',
    labels = data['Coding Level'],
    autopct = '%1.4f%%', # 소수점 넷째 자리까지 나타내기
    figsize = (6, 6),
    legend = True, # 범례
    title = 'Coding Level / Other Language Experience'
).get_figure()
st.pyplot(fig)
