
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

  
def test_group(app):
    app.Login("admin", "secret")
    app.Create_Group(Group(name="jgfjyuygiuy", header="kgkhkj", footer="kgkhlij;"))
    app.Logout()
def test_empty_group(app):
    app.Login("admin", "secret")
    app.Create_Group(Group(name="", header="", footer=""))
    app.Logout()
