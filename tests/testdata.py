'''Testing the Faker test data generation'''
import pytest
from decimal import Decimal
from faker import Faker

fake = Faker()


def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of test records to generate")
