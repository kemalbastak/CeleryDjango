import datetime

from .models import Tasks
from faker import Faker
from datetime import date, timedelta
import random
fake = Faker('tr_TR')
def func():
    data = dict(
        user=fake.name(),
        assignee=fake.name(),
        task_name=fake.job(),
        email=fake.email(),
        due_date=date(2021, 11, 12) + timedelta(days=random.randint(1, 15)))

    task = Tasks(**data)

    task.save()
"""
dueDate = "17.11.2021"

dueDateStr = datetime.datetime.strptime(dueDate, '%d.%m.%Y').strftime('%Y-%m-%d')
dueDateDate = datetime.datetime.strptime(dueDateStr, '%Y-%m-%d').date()
today = datetime.date.today()
diff = (dueDateDate-today).days
if diff==5:
    print("5 gün kaldı")
"""