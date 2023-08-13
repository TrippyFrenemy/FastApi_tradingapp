# App using FastApi Framework
This project was created so that I could learn a new framework in it


## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.
```bash
pip install -r requirements.txt
```


## To start project with celery
### !!!Before start use pip to install requirements!!!
Create some processes of bash
Celery for background tasks
```bash
celery -A src.tasks.tasks:celery worker --loglevel=INFO --pool=solo
```
Flower for celery ui
```bash
celery -A src.tasks.tasks:celery flower
```
The start of the app
```bash
uvicorn main:app --reload
```


## To start tests
All tests uses pytest and all of them are in tests/ library
```bash
pytest -s -v tests/
```
