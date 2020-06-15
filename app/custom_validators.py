from marshmallow.validate import Validator, ValidationError
from mongoengine import Document
import typing


class Unique(Validator):
    """Validator which succeeds if the value passed to it is unique.

    :param model: The model.
    :param attr: The attribute.
    :param error: Error message to raise in case of a validation error.
    """

    message = "The value has been taken."

    def __init__(
            self, model: Document, attr: str, *, error: str = None
    ):
        self.model = model
        self.attr = attr
        self.error = error

    def _repr_args(self) -> str:
        return "model={!r}, attr={!r}".format(self.attr, self.model.__class__.__name__)

    def _format_error(self, value, message: str) -> str:
        return self.error or message

    def __call__(self, value) -> typing.Any:
        filter_args = {self.attr: value}
        if self.model.objects(**filter_args).first() is not None:
            raise ValidationError(self._format_error(value, self.message))

        return value
