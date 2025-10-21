from django.db import connections
from django.db.utils import OperationalError
import time


def wait_for_db():
    db_conn = connections['default']
    while True:
        try:
            db_conn.cursor()
            break
        except OperationalError:
            print("Postgres unavailable, waiting 1 second...")
            time.sleep(1)
