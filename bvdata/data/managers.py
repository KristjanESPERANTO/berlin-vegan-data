from datetime import timedelta

from django.db import models
from django.db.models import Q
from django.db.models.functions import Lower
from django.utils import timezone


class GastroQuerySet(models.QuerySet):
    def api(self):
        return self.filter(
            Q(closed__isnull=True)
            | Q(vegan=5, closed__gte=timezone.now() - timedelta(weeks=21))
        )

    def open(self):
        return self.filter(closed__isnull=True)

    def closed(self):
        return self.filter(closed__isnull=False)

    def alphabetical(self):
        return self.order_by(Lower("name"))
