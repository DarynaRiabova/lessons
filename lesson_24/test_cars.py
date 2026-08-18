import logging

import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    handlers=[
        logging.FileHandler("test_search.log", mode="w"),
        logging.StreamHandler(),
    ],
    force=True,
)

logger = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()
    response = session.post(
        f"{BASE_URL}/auth", auth=HTTPBasicAuth("test_user", "test_pass")
    )
    assert response.status_code == 200
    token = response.json()["access_token"]
    session.headers.update({"Authorization": "Bearer " + token})
    return session


class TestCarsSearch:
    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            ("price", 5),
            ("year", 3),
            ("brand", 10),
            ("engine_volume", 7),
            ("price", 2),
        ],
    )
    def test_search_cars(self, auth_session, sort_by, limit):
        logger.info(f"sort_by={sort_by}, limit={limit}")
        response = auth_session.get(
            f"{BASE_URL}/cars", params={"sort_by": sort_by, "limit": limit}
        )
        assert response.status_code == 200
        cars = response.json()
        assert len(cars) == limit
        logger.info("Test passed")
