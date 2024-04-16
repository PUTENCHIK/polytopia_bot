import pytest
from polytopia_bot.models.BordurBot import BordurBot


def test_bordur_1():
    bot = BordurBot("Danny", 5)
    assert bot.complexity_definition() == "Impossible"
