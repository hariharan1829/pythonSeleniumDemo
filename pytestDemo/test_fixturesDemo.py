# -------------------------------------------------------------
# ⚙️ Pytest Fixtures and Parameterization - Notes
# -------------------------------------------------------------
# ✅ Fixtures are reusable pieces of setup and teardown code.
#    - Code before 'yield' runs *before* each test (setup).
#    - Code after 'yield' runs *after* each test (teardown).
#
# ✅ Fixtures can be used across multiple test files if defined in `conftest.py`.
#    - `conftest.py` acts as a shared configuration file.
#
# ✅ Classes can use fixtures with:
#       @pytest.mark.usefixtures("fixture_name")
#    This automatically applies the fixture to every test method in that class.
#
# ✅ You can also pass fixtures as method parameters to access their return values.
#
# ✅ Parametrized fixtures allow running the same test with multiple data sets.
#    Example: @pytest.fixture(params=[("chrome", "Hari"), ("firefox", "Haran")])
# -------------------------------------------------------------

import pytest

# -------------------------------------------------------------
# 🧩 Example of Fixture Usage (setup and teardown)
# -------------------------------------------------------------
# Uncomment below lines if you want to see setup/teardown behavior
# @pytest.fixture()
# def setup():
#     print("I will be executed first (setup)")
#     yield
#     print("I will be executed last (teardown)")

# -------------------------------------------------------------
# 🧪 Using a fixture for an entire class
# -------------------------------------------------------------
@pytest.mark.usefixtures("setup")
class TestFixtures:

    def test_morningGreet1(self):
        print("Good Morning all")

    def test_morningGreet2(self):
        print("Good Morning all")

    def test_morningGreet3(self):
        print("Good Morning all")


# -------------------------------------------------------------
# 🧠 Using fixture in a single test (method-level)
# -------------------------------------------------------------
def test_morningGreet5(setup):
    print("Good Night")


# -------------------------------------------------------------
# 📦 Fixture that provides test data (sendData)
# -------------------------------------------------------------
# Here, we assume "sendData" is defined in conftest.py.
# The fixture returns some form of test data (like a list or tuple).
@pytest.mark.usefixtures("sendData")
class TestProfileData:

    def test_greeting(self, sendData):
        # Accessing the 3rd value from sendData and printing it
        print(sendData[2])


# -------------------------------------------------------------
# 🌐 Using the Parametrized Fixture (crossBrowser)
# -------------------------------------------------------------
# This test will execute 3 times:
#   1. ("chrome", "Hari")
#   2. ("firefox", "Haran")
#   3. ("IE", "Selvaraj")
def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
