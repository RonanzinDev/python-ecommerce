import pytest
from httpx import AsyncClient

from ecommerce.auth.jwt import create_access_token
from conf_test_db import app

@pytest.mark.asyncio
async def test_all_users():
    async with AsyncClient(app=app, base_url="http://test") as client:
        user_access_token = create_access_token({"sub": "morellianogm@gmail.com"})
        response =  await client.get("/user/", headers={"Authorization": f"Bearer {user_access_token}"})
    
    assert response.status_code == 200
    