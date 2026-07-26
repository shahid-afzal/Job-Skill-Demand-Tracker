from src.fetcher import validate_response


class FakeResponse:
    def __init__(self, data):
        self.data = data

    def json(self):
        return self.data


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


fake_response = FakeResponse(response_data)

print(validate_response(fake_response))

fake_response = FakeResponse(no_result)

print(validate_response(fake_response))

fake_response = FakeResponse(error)

try:
    print(validate_response(fake_response))
except Exception as e:
    print(f"Test passed — correctly caught error: {e}")