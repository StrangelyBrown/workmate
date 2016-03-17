from django.core.urlresolvers import reverse
from django.test import TestCase

from .mixins import AuthTestMixin


class MainTests(AuthTestMixin, TestCase):

    def get_url(self):
        return reverse('workmate-main')