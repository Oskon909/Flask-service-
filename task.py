from app import app
from celery_config import make_celery
from parsing import run_pars_selexy

celery = make_celery(app)



# Периодичный парсинг
@celery.task(name="periodic_task2")
def periodic_task2():
    run_pars_selexy()
    print('Hi! from periodic_task2')


@celery.task(name="periodic_task")
def periodic_task():
    print('Hi! from periodic_task')

