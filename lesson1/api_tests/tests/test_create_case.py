from utils.api_client import client
import pytest
from services.case.data import positive_create_case
from services.case.pom import create_case

@pytest.mark.parametrize('data', positive_create_case)
def test_create_case_positive(data):
    response = create_case(json=data)

    response.status_code_should_be_eq(200)
    response.json_should_be_eq(data)
