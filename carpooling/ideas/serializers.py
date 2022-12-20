from django.core.serializers.json import DjangoJSONEncoder

from carpooling.ideas.models import User


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return str(obj)
        return super().default(obj)