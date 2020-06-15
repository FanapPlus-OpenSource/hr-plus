from datetime import datetime
from app.db import db
from app.custom_query_sets import SoftDeleteQuerySet
from mongoengine import StringField, DateTimeField, EmailField, BooleanField
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Document):
    meta = {'queryset_class': SoftDeleteQuerySet, 'collection': 'users'}

    first_name = db.StringField()
    last_name = StringField()
    date_joined = DateTimeField(required=True)
    email = EmailField(required=True, unique=True)
    password_hash = StringField(required=True, min_length=6)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    deleted_at = DateTimeField(null=None)

    @property
    def full_name(self):
        if self.first_name.strip() != '' and self.last_name.strip() != '':
            return "{} {}".format(self.first_name.strip(), self.last_name.strip())
        if self.first_name.strip() != '':
            return self.first_name.strip()
        if self.last_name.strip() != '':
            return self.last_name.strip()
        return self.email.strip()

    def set_password_hash(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
