import factory
from factory.django import DjangoModelFactory
from .. import models


class AccountFactory(DjangoModelFactory):

    # pylint: disable=R0903
    class Meta:
        model = models.Account

    username = factory.Faker('user_name')
    email = factory.LazyAttribute(
        lambda f: '{0}.{1}@example.com'.format(
            f.first_name, f.last_name
        ).lower()
    )
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_staff = False
    is_superuser = False
    password = factory.Faker('password')

