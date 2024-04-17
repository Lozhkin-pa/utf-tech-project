
# 🍽️ Restaurant Project 
## _UTF.tech test project_

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

Проект представляет собой веб-приложение для ресторана. Реализован эндпоинт /api/v1/foods/, отображающий список категорий и блюд:
* В выборку попадают только категории с блюдами, у которых is_publish=True
* Если в категории нет блюд - в выборку не вкючается
* Если в категории все блюда is_publish=False - в выборку не вкючается

### __Установка на локальном компьютере__
1. Клонируйте репозиторий:
    ```
    git clone git@github.com:Lozhkin-pa/utf-tech-project.git
    ```
2. Установите и активируйте виртуальное окружение:
    ```
    python -m venv venv
    source venv/Scripts/activate  - для Windows
    source venv/bin/activate - для Linux
    ```
3. Установите зависимости:
    ```
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
4. Перейдите в папку restaurant и выполните миграции:
    ```
    cd restaurant
    python manage.py migrate
    ```
5. Запустите проект:
    ```
    python manage.py runserver
    ```
### __Загрузка фикстур__
Из директории /restaurant/ выполните загрузку фикстур:
```
python manage.py loaddata menu/fixtures/food_fixtures.json
```
### __Примеры запросов__

<details><summary> GET: http://127.0.0.1:8000/api/v1/foods/ - показать список категорий с блюдами.</summary>

    200 OK:
    ```
    [
    {
        "id": 1,
        "name_ru": "Напитки",
        "name_en": null,
        "name_ch": null,
        "order_id": 10,
        "foods": [
            {
                "internal_code": null,
                "code": 1,
                "name_ru": "Чай",
                "description_ru": null,
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "123.00",
                "additional": []
            },
            {
                "internal_code": null,
                "code": 2,
                "name_ru": "Спрайт",
                "description_ru": null,
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "123.00",
                "additional": []
            },
            {
                "internal_code": null,
                "code": 4,
                "name_ru": "Байкал",
                "description_ru": null,
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "123.00",
                "additional": []
            }
        ]
    },
    {
        "id": 2,
        "name_ru": "Выпечка",
        "name_en": null,
        "name_ch": null,
        "order_id": 10,
        "foods": [
            {
                "internal_code": null,
                "code": 5,
                "name_ru": "Булочка с маком",
                "description_ru": null,
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "123.00",
                "additional": []
            }
        ]
    }
    ]
    ```
</details>

### __Технологии__
* [Python 3.10.12](https://www.python.org/doc/)
* [Django 5.0.4](https://docs.djangoproject.com/)
* [Django REST Framework 3.15.1](https://www.django-rest-framework.org/)

### __Автор__
[Павел Ложкин](https://github.com/Lozhkin-pa)
