# Run all test found in matching files test_* or *_test
pytest

# Run tests in a module
pytest "test_mod.py"

# Run tests in a folder
pytest .\day-04\nested_with_tests\

# Filter with keyword
pytest -k "one and not two"

# Run a specific test with name
pytest .\day-04\nested_with_tests\nested_test.py::test_one