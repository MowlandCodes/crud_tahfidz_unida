from django.contrib.auth.models import User
from django.db import models
import uuid

if not hasattr(User, "uuid"):
    User.add_to_class("uuid", models.UUIDField(default=uuid.uuid4, editable=False, unique=True))
