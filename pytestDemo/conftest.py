import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed 1st")
    yield
    print("I will be executed last")

@pytest.fixture(scope="class")
def sendData( ):
    print("Send data to profile")
    return ["Hariharan", "Selvaraj", "hariharan.s.246@gmail.com"]

# -------------------------------------------------------------
# 🔁 Example of a Parametrized Fixture
# -------------------------------------------------------------
# This fixture will run the test multiple times with different values.
# Each tuple contains (browser_name, user_name).
@pytest.fixture(params=[("chrome", "Hari"), ("firefox", "Haran"), ("IE", "Selvaraj")])
def crossBrowser(request):
    # Return the current parameter (browser and user)
    return request.param