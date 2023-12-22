# PI_Final
The final project in the discipline "Software Engineering" of UrFU
Russian Russian text translation application for English to English and Russian to English.    
It is intended to help you work with texts in a foreign language (Reading documentation, preparing letters...)

## TranslaterML

### Launching the application

To run the application, you need to install the dependencies and run the uvicorn and streamlit:
 - Installing dependencies
```bash
pip install -r requirements.txt
```
 - run the FastAPI application (Linux)
```bash
uvicorn  fastapi_app:app
```
- run the FastAPI application (Windows)
```bash
python -m uvicorn  fastapi_app:app
```
 - run the streamlit application
```bash
streamlit run stream_app.py
```
- run the test
```bash
pytest test_main.py
```

#### The following ready-made models were used:
Helsinki-NLP/opus-mt-en-ru     
Helsinki-NLP/Opus-mt-ru-en

@InProceedings{TiedemannThottingal:EAMT2020,
  author = {J{\"o}rg Tiedemann and Santhosh Thottingal},
  title = {{OPUS-MT} — {B}uilding open translation services for the {W}orld},
  booktitle = {Proceedings of the 22nd Annual Conferenec of the European Association for Machine Translation (EAMT)},
  year = {2020},
  address = {Lisbon, Portugal}

# PI_Final
Итоговый проект по дисциплине "Программная инженерия" УрФУ.   
Приложение для перевода текста с английского на русский и русского на английский.   
Предназначено для помощи в  работе с текстами на иностранном языке (Чтение документации, подготовка писем...)   

## TranslaterML

### Запуск приложения

Чтобы запустить приложение, вам необходимо установить зависимости и запустить uvicorn:

 - Установка зависимостей
```bash
pip install -r requirements.txt
```
 - Запуск приложения FastAPI (Linux)
```bash
uvicorn  fastapi_app:app
```
 - Запуск приложения FastAPI (Windows)
```bash
python -m uvicorn  fastapi_app:app
```
 - Запуск приложения application
```bash
streamlit run stream_app.py
```
- Запуск тестирования
```bash
pytest test_main.py
```

### Были использованы следующие готовые модели:
Helsinki-NLP/opus-mt-en-ru    
Helsinki-NLP/Opus-mt-ru-en
