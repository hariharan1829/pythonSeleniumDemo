# ---------------------------------------------
# Pytest Basics
# ---------------------------------------------
# ✅ File Naming:
#    - The file name must start with 'test_' or end with '_test'
#
# ✅ Function Naming:
#    - Each test method must start with 'test_'
#    - Each method name should describe its purpose
#
# ✅ Running Tests:
#    1. Run all tests in a directory:
#         py.test -v -s
#    2. Run a specific file:
#         py.test test_filename.py -v -s
#    3. Run a specific test method:
#         py.test -k method_name -v -s
#    4. Run specific tagged tests:
#         py.test -m smoke -v -s
#
# ✅ Pytest Markers:
#    - @pytest.mark.smoke → marks a test as part of the smoke suite
#    - @pytest.mark.skip → skips the test
#    - @pytest.mark.xfail → marks a test that is expected to fail
# ---------------------------------------------

import pytest



def test_first_program():
    print("Hello from the first test!")

@pytest.mark.skip
def test_greet():
    print("Good Morning!")

@pytest.mark.smoke
def test_greet_credit(setup):
    print("Good Evening!")
