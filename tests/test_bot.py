import pytest
from polytopia_bot.models.Bot import Bot


def test_1():
    bot = Bot("test", 1)
    assert bot.complexity_definition() == 'Low skill'
