''' Скрипт добавляет рыбу в БД.'''
from django_seed import Seed
from .models import Question, Answer
from django.contrib.auth.models import User


seeder = Seed.seeder()

seeder.add_entity(User, 10)
seeder.add_entity(Question, 50)
seeder.add_entity(Answer, 300)

