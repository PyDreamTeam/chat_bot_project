class AuthTestMixin:

    def get_headers_for_auth(self, email, password):
        data = {"email": email, "password": password}
        response = self.client.post("/api/auth/jwt/create", data)
        token = response.json()["access"]
        return {
            "HTTP_CONTENT_TYPE": "application/json",
            "HTTP_AUTHORIZATION": f"JWT {token}",
        }
