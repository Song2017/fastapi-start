# coding: utf-8

from fastapi.testclient import TestClient




def test_get_health(client: TestClient):
    """Test case for get_health

    health
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/health",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

