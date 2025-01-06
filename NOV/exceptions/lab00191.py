import pytest


@pytest.fixture()
def is_married_before_run():
    return False


def test_update(is_married_before_run):
    assert is_married_before_run == True