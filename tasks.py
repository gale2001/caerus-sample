from celery import Celery
from caerus import setup
from sqlalchemy import MetaData, create_engine

meta = MetaData(bind=create_engine('sqlite:///sample.db'))
setup(meta)
meta.create_all()

# app = Celery('caerus-sample', broker='amqp://guest@localhost//')
app = Celery('caerus-sample', broker='sqla+sqlite:///celery-broker.db')

@app.task
def hoge(msg='hoge'):
    print msg
