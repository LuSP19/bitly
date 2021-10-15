# Обрезка ссылок с помощью Битли

Скрипт позволяет сокращать ссылки с помощью сервиса [Bitly](https://app.bitly.com/), а также отслеживать количество переходов по полученным коротким ссылкам.

### Как установить

Для использования скрипта понадобится учётная запись [Bitly](https://bitly.com/a/sign_up), а также токен (ключ) вида `cbd2a37eca3b5eceadefa632b434b0ab52af35a7`, который можно получить на странице с [настройками](https://app.bitly.com/settings/api/) вашего профиля.
Токен нужно поместить в файл **.env** в каталоге со скриптом в следующем виде:

```bash
BITLY_TOKEN='cbd2a37eca3b5eceadefa632b434b0ab52af35a7'
```
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

### Запуск

Просто запустите скрипт указав ссылку для сокращения в качестве аргумента:
```bash
python3 main.py http://google.com
https://bit.ly/3itiVT1
```
или укажите существующую короткую ссылку для проверки переходов:
```bash
python3 main.py bit.ly/3itiVT1
Количество переходов по ссылке битли: 1
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
