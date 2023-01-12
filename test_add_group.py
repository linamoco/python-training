# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()                # создаем фикстуру
    request.addfinalizer(fixture.destroy)  # удаляем фикустуру с помощью функции инициализации фикстуры
    return fixture

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()


def test_add_empty_group(app):
    app.login(username="", password="")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
