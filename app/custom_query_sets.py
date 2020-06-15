from flask_mongoengine import BaseQuerySet


class SoftDeleteQuerySet(BaseQuerySet):

    def get_not_trashed(self):
        return self.filter(deleted_at=None)

    def get_trashed(self):
        return self.filter(deleted_at__ne=None)
