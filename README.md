# country_details

Authentication Overview
This API uses Token Authentication. You must first obtain a token using your username and password. Then include the token in the header of every request to access protected endpoints.

1. 🔑 Obtain Auth Token
Endpoint: POST /api-token-auth/

Description: Log in with username and password to get an authentication token.

Request Body (JSON):
