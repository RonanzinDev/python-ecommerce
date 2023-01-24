import pytest

from ecommerce.user.models import User

@pytest.fixture(autouse=True)
def create_dummy_user(tmpdir):
    from conf_test_db import override_get_db
    database = next(override_get_db())
    new_user = User(name="Gabriel", email="morellianogm@gmail.com", password='12345678')
    database.add(new_user)
    database.commit()
    
    
    yield #this is where the testing happens
    
    #teardown(dps do teste acabar ele vai deletar o usuario)
    database.query(User).filter(User.email == "morellianogm@gmail.com").delete()
    database.commit()