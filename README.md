# Пульт охраны хранилища

Веб-сервис создан для контроля и мониторинга доступа сотрудников к хранилищу в банке.

## active_passcards_view.py

Содержит в себе функцию `active_passcards_view`, принимающую `request` и возвращающая `active_passcards.html` страницу со всеми активными картами доступа.

## passcard_info_view.py

Содержит в себе функцию `passcard_info_view`, принимающую `request` и `passcode`, где `passcode` - это код пропуска. Скрипт возвращает историю посещений сотрудника с полями:

- Дату и время посещения;
- Продолжительность посещения;
- Подозрительность визита (True, если более часа).

## storage_information_view.py

Содержит в себе функцию `storage_information_view`, принимающую `request`. Возвращает всех сотрудников, которые в данный момент находятся в хранилище с полями:

- Имя посетителя;
- Время входа;
- Длительность пребывания;
- Подозрительность.

### Как установить

Требуемые ключи для окружения:
- DB_HOST - Хост базы данных;
- DB_PORT - Порт базы данных;
- DB_NAME - Имя базы данных;
- DB_USER - Логин от базы данных;
- DB_PASSWORD - Пароль от базы данных.

Опциональные ключи для окружения:
- SECRET_KEY - Секретный ключ. По стандарту - 123;
- DEBUG - Режим отладки. По стандарту - True;
- ALLOWED_HOSTS - Допустимые хосты. По стандарту - *

Пример .env:

```
export DB_HOST=checkpoint.devman.org
export DB_PORT=5434
export DB_NAME=checkpoint
export DB_USER=guard
export DB_PASSWORD=osim5
export SECRET_KEY=REPLACE_ME
export DEBUG=false
export ALLOWED_HOSTS=*
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).