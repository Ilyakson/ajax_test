import os

import pytest


@pytest.mark.parametrize(
    "email,password,expected",
    [
        pytest.param(
            os.getenv("EMAIL"),
            os.getenv("PASSWORD"),
            True,
            id="Successful Authentication",
        ),
        pytest.param(
            os.getenv("EMAIL"),
            "test_password123",
            False,
            id="Authentication with incorrect password",
        ),
        pytest.param(
            "test_email123@test.test",
            os.getenv("PASSWORD"),
            False,
            id="Authentication with incorrect email",
        ),
        pytest.param(
            "",
            os.getenv("PASSWORD"),
            False,
            id="Authentication without email"
        ),
        pytest.param(
            os.getenv("EMAIL"),
            "",
            False,
            id="Authentication without password",
        ),
        pytest.param(
            "",
            "",
            False,
            id="Authentication with empty fields"
        ),
    ],
)
def test_user_login(email: str, password: str, expected, user_login_fixture):
    page = user_login_fixture
    page.login_user(email, password)
    assert page.user_on_main_page() == expected
