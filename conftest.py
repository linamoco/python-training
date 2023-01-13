import pytest
from fixture.application import Application

@pytest.fixture(scope="session")
def app(request):
    fixture = Application()                # создаем фикстуру
    request.addfinalizer(fixture.destroy)  # удаляем фикстуру с помощью функции инициализации фикстуры
    return fixture