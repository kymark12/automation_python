import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will run last")


@pytest.fixture()
def data_load():
    print("User data is being created")
    return ["Mark", "Ivan", "ivan.berbenzana@zenrooms.com"]


@pytest.fixture(params=[("chrome", "Ivan", "Marky"), ("Firefox", "Hello_World"), ("IE", "Edge")])
def crossbrowser(request):
    return request.param
