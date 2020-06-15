# Model Schemas
from app.extensions import ma
from marshmallow import fields as flds


class FullUserSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "email", "first_name", "last_name", "full_name", "date_joined", "is_active", "is_staff",
                  "is_superuser")

    id = flds.String(attribute="id")


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = (
            "id", "first_name", "last_name", "full_name", "date_joined", "is_active", "is_staff",
            "is_superuser")

    id = flds.String(attribute="id")
