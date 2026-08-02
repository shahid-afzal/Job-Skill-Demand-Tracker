from src.fetcher import validate_response


class FakeResponse:
    """A mock implementation of a requests.Response object for unit testing."""

    def __init__(self, data):
        """Initializes FakeResponse with pre-defined response data.

        Args:
            data (dict): The mock response dictionary to return from json().
        """
        self.data = data

    def json(self):
        """Mocks the json() method of requests.Response.

        Returns:
            dict: The mock response data dictionary.
        """
        return self.data


# Mock payload scenarios representing valid, empty, and error responses
response_data = {
    "results": [
        {
            "title": "Python Developer"
        }
    ]
}

no_result = {
    "results": []
}

error = {
    "error": "API Error"
}


# Test 1: Validate a standard successful response
fake_response = FakeResponse(response_data)
print(validate_response(fake_response))

# Test 2: Validate a response that contains an empty results list
fake_response = FakeResponse(no_result)
print(validate_response(fake_response))

# Test 3: Validate a response containing an error key (expects Exception)
fake_response = FakeResponse(error)

try:
    print(validate_response(fake_response))
except Exception as e:
    # Verify that the correct Exception is thrown and caught
    print(f"Test passed — correctly caught error: {e}")
