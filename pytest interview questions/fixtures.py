# ✅ What are fixtures in pytest?
import pytest

# Fixtures in pytest are used to set up and tear down test environments automatically.
# They help in initializing test data, configurations, or resources before a test runs,
# and cleaning them up after the test completes.

# 🔹 Advantages of using fixtures:
# 1. Reusability – The same fixture can be used across multiple tests.
# 2. Automatic setup and teardown – Code before `yield` runs before the test,
#    and code after `yield` runs after the test.
# 3. Scope control – You can define how often a fixture runs (per test, per class, per module, per session).
# 4. Dependency injection – Fixtures can be passed as arguments to test functions automatically.

# Tag used to define a fixture: @pytest.fixture
#Tag used : @pytest.fixture

@pytest.fixture()
def dataPersonnel():
    print("executes 1st")
    sample_data = {"name": "Hari", "age":"10" }
    yield  sample_data
    print("function closed")

def test_sampledata(dataPersonnel):
    assert dataPersonnel["name"] == "Hari"
