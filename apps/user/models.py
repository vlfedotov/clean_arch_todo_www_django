# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models

from todo.user import User as ExtUser
from todo.todo import Todo as ExtTodo


class User(ExtUser, models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Todo(ExtTodo, models.Model):
    todo = models.CharField(max_length=255)
    created = models.DateTimeField(default=datetime.now)
    is_done = False
    user = models.ForeignKey(User)
