import datetime
import factory
import factory.fuzzy
import random

from covid_dashboard.models.cases_details import CasesDetails
from covid_dashboard.models.mandal import Mandal
from covid_dashboard.models.district import District
from covid_dashboard.models.state import State
from covid_dashboard.models.user import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: "user %d" %n)
    name = "John"

class StateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = State
    state_name = factory.Sequence(lambda n: "state %d" %n)

class DistrictFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = District
    state = factory.SubFactory(StateFactory)
    district_name = factory.Sequence(lambda n: "district %d" %n)

class MandalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Mandal
    district = factory.SubFactory(DistrictFactory)
    mandal_name = factory.Sequence(lambda n: "mandal %d" %n)

class CasesDetailsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CasesDetails
    mandal = factory.SubFactory(MandalFactory)
    date = factory.LazyFunction(datetime.date.today)
    confirmed_cases = factory.fuzzy.FuzzyInteger(0, 1000)
    recovered_cases = factory.fuzzy.FuzzyInteger(0, 1000)
    deaths = factory.fuzzy.FuzzyInteger(0, 1000)
