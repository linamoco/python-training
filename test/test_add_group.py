# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()                # создаем фикстуру
    request.addfinalizer(fixture.destroy)  # удаляем фикустуру с помощью функции инициализации фикстуры
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="dfdfdf", header="dfdfdfd", footer="dffdf"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()



