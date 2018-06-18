# COPLA
![COPLA](https://github.com/otamans/copla-web/blob/master/frontend/img/logo.png)


## Запуск API

1. Клонировать репозиторий

2. Установить python3

    `sudo apt-get install python3.6

3. Инициализировать [`virtualenv`](http://pypi.python.org/pypi/virtualenv)

    `sudo apt-get install python3-venv`

    `python3 -m venv ENV_NAME`

    и ввести

    `. ENV_NAME/bin/activate`

4. `pip install -r requirements.txt` 

5. Запустить миграции db:

    `python manage.py migrate`

6. Запустить `python manage.py runserver` и открыть [http://localhost:8000](http://localhost:8000)

