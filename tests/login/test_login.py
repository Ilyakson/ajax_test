import pytest


@pytest.mark.parametrize(
    "email,password,expected",
    [
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_password",
            True,
            id="Successful Authentication",
        ),
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "test_password123",
            False,
            id="Authentication with incorrect password",
        ),
        pytest.param(
            "test_email123@test.test",
            "qa_automation_password",
            False,
            id="Authentication with incorrect email",
        ),
        pytest.param(
            "",
            "qa_automation_password",
            False,
            id="Authentication without email"
        ),
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
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
