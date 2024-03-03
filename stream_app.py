import streamlit as st
import requests
import json

# Заголок
st.title('Перевод текста')

# поле для ввода оригинала текста
buf_orig_text = st.text_input("Введите текс для перевода (Enter the English text here):")
# направление перевода
status = st.radio("Направление перевода: ", ('EN->RU', 'RU->EN'))
orig_text = {'text': buf_orig_text.title()}
# при нажатии кнопки
if (st.button('Translate')):

    # перевод с русского на англиский
    if (status == 'RU->EN'):
        response = requests.post(url="http://127.0.0.1:8000/ru-en/", data=json.dumps(orig_text))
    # перевод с англиского на русский
    else:
        response = requests.post(url="http://127.0.0.1:8000/en-ru/", data=json.dumps(orig_text))
    st.success(response.text)
