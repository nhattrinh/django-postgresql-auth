from django.contrib.auth import models
from django.contrib.postgres.fields import ArrayField, CharField
from django.db import models as db_models
import uuid

class User(models.User):
    # basic User fields
    email = CharField(max_length = 150)
    first_name = CharField(max_length = 30)
    last_name = CharField(max_length = 30)
    password = CharField(max_length = 150)
    
    # primary key id, unique and not null
    id = db_models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # add more fields down here

