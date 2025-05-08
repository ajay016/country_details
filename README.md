# country_details

## Installation
Follow the steps below to get this project up and running on your local machine.

## Requirements
Python 3.10+

pip (Python package manager)

Git (optional, for cloning the repo)

## Setup Instructions
Create and activate a virtual environment
    `python -m venv venv`
    `source venv/bin/activate`      # For Linux/macOS
    `venv\Scripts\activate`       # For Windows


### Install dependencies:
This project uses Django 5 and Django REST Framework. All required packages are listed in requirements.txt. Install them with:
    `pip install -r requirements.txt`

### Apply database migrations:
`python manage.py makemigrations`
`python manage.py migrate`

### Create a superuser account:
This is used to access the Django admin panel.
    `python manage.py createsuperuser`


### Access the application:
Open your browser and go to http://127.0.0.1:8000/ to view the app.
Go to http://127.0.0.1:8000/admin/ to access the admin panel.
Go to http://127.0.0.1:8000/api/<API endpoints> to access the API endpoints.

### Tech Stack
Python 3.10+
Django 5
Django REST Framework – Used for building secure and modular API endpoints.
SQLite – Default database (can be replaced with PostgreSQL or others).



# Authentication
This project uses Django’s built-in authentication system to access certain pages and Django Rest Framework to restrict accesss to API endpoints.

### Login (via Web)
Visit the login page at:
http://localhost:8000/login/

Use a registered username and password to log in.

After login, users are redirected to the home page.

### Logout
To log out, click the Logout button in the navigation bar.
You will be redirected to the login page.


# Accessing API endpoints
### Obtain Token
    Endpoint:
    POST http://127.0.0.1:8000/api/api-token-auth/

    Headers: `Content-Type: application/x-www-form-urlencoded`
    Body (form-data or x-www-form-urlencoded): 
        username=your_username
        password=your_password

Response from the server:
```
    {
        "token": "your_generated_token"
    }
```

### Use the Token in API Requests
Once you obtain the token, include it in the Authorization header of subsequent API requests:
Header: `Authorization: Token your_generated_token`

Example with curl:
`curl -H "Authorization: Token your_generated_token" http://127.0.0.1:8000/api/country-details/bgd/`


# GET `/api/country-list/` — Get Country List
Description:
Retrieves all countries in a list format.
This endpoint requires authentication via a token.

🔐 Authentication Required
You must include a valid Token in the request header.

Token is obtained by logging in through /api-token-auth/ (or your token URL if different).

`Authorization: Token your_token_here`

## Request
Method: GET
URL: /api/country-list/


# GET /api/country-details/<cca3>/ — Get Country Details
Description:
Retrieves details of a specific country using its cca3 (3-letter country code).
Authentication with token is required.

🔐 Authentication Required
You must include a valid Token in the request header.

Header Example: `Authorization: Token your_token_here`


## Request
Method: GET
URL: /api/country-details/<cca3>/
Replace <cca3> with the actual 3-letter country code.
Example: /api/country-details/USA/

Headers: `Authorization: Token your_token_here`


## Response (200 OK)
```
{
  "name_common": "United States",
  "cca3": "USA",
  "region": "Americas",
  "population": 331893745,
  "languages": ["English"]
}
```


# POST /api/create-country/ — Create a New Country
Description: Creates a new country entry. Requires authentication via token.

Authentication Required
You must include a valid Token in the request header.

Header Example: `Authorization: Token your_token_here`


## Request
Method: POST
URL: /api/create-country/

Headers:
```
Authorization: Token your_token_here
Content-Type: application/json
```

### Body (JSON):
```
{
        "name": {
            "common": "Test1",
            "official": "Republic of Test",
            "nativeName": {
                "eng": {
                    "official": "Republic of Test",
                    "common": "Botswana"
                },
                "tsn": {
                    "official": "Lefatshe la Botswana",
                    "common": "Test"
                }
            }
        },
        "tld": [
            ".bw"
        ],
        "cca2": "Te",
        "ccn3": "072",
        "cioc": "BOT",
        "independent": true,
        "status": "officially-assigned",
        "unMember": true,
        "currencies": {
            "BWP": {
                "symbol": "P",
                "name": "Botswana pula"
            }
        },
        "idd": {
            "root": "+2",
            "suffixes": [
                "67"
            ]
        },
        "capital": [
            "Gaborone"
        ],
        "altSpellings": [
            "BW",
            "Republic of Botswana",
            "Lefatshe la Botswana"
        ],
        "region": "Africa",
        "subregion": "Southern Africa",
        "languages": {
            "eng": "English",
            "tsn": "Tswana"
        },
        "latlng": [
            -22.0,
            24.0
        ],
        "landlocked": true,
        "borders": [
            "NAM",
            "ZAF",
            "ZMB",
            "ZWE"
        ],
        "area": 582000.0,
        "demonyms": {
            "eng": {
                "f": "Motswana",
                "m": "Motswana"
            },
            "fra": {
                "f": "Botswanaise",
                "m": "Botswanais"
            }
        },
        "cca3": "TES",
        "translations": {
            "ara": {
                "official": "جمهورية بوتسوانا",
                "common": "بوتسوانا"
            },
            "bre": {
                "official": "Republik Botswana",
                "common": "Botswana"
            },
            "ces": {
                "official": "Botswanská republika",
                "common": "Botswana"
            },
            "cym": {
                "official": "Republic of Botswana",
                "common": "Botswana"
            },
            "deu": {
                "official": "Republik Botsuana",
                "common": "Botswana"
            },
            "est": {
                "official": "Botswana Vabariik",
                "common": "Botswana"
            },
            "fin": {
                "official": "Botswanan tasavalta",
                "common": "Botswana"
            },
            "fra": {
                "official": "République du Botswana",
                "common": "Botswana"
            },
            "hrv": {
                "official": "Republika Bocvana",
                "common": "Bocvana"
            },
            "hun": {
                "official": "Botswanai Köztársaság",
                "common": "Botswana"
            },
            "ind": {
                "official": "Republik Botswana",
                "common": "Botswana"
            },
            "ita": {
                "official": "Repubblica del Botswana",
                "common": "Botswana"
            },
            "jpn": {
                "official": "ボツワナ共和国",
                "common": "ボツワナ"
            },
            "kor": {
                "official": "보츠와나 공화국",
                "common": "보츠와나"
            },
            "nld": {
                "official": "Republiek Botswana",
                "common": "Botswana"
            },
            "per": {
                "official": "جمهوری بوتسوانا",
                "common": "بوتسوانا"
            },
            "pol": {
                "official": "Republika Botswany",
                "common": "Botswana"
            },
            "por": {
                "official": "República do Botswana",
                "common": "Botswana"
            },
            "rus": {
                "official": "Республика Ботсвана",
                "common": "Ботсвана"
            },
            "slk": {
                "official": "Botswanská republika",
                "common": "Botswana"
            },
            "spa": {
                "official": "República de Botswana",
                "common": "Botswana"
            },
            "srp": {
                "official": "Република Боцвана",
                "common": "Боцвана"
            },
            "swe": {
                "official": "Republiken Botswana",
                "common": "Botswana"
            },
            "tur": {
                "official": "Botsvana Cumhuriyeti",
                "common": "Botsvana"
            },
            "urd": {
                "official": "جمہوریہ بوٹسوانا",
                "common": "بوٹسوانا"
            },
            "zho": {
                "official": "博茨瓦纳共和国",
                "common": "博茨瓦纳"
            }
        },
        "flag": "🇧🇼",
        "maps": {
            "googleMaps": "https://goo.gl/maps/E364KeLy6N4JwxwQ8",
            "openStreetMaps": "https://www.openstreetmap.org/relation/1889339"
        },
        "population": 2351625,
        "gini": {
            "2015": 53.3
        },
        "fifa": "BOT",
        "car": {
            "signs": [
                "BW"
            ],
            "side": "left"
        },
        "timezones": [
            "UTC+02:00"
        ],
        "continents": [
            "Africa"
        ],
        "flags": {
            "png": "https://flagcdn.com/w320/bw.png",
            "svg": "https://flagcdn.com/bw.svg",
            "alt": "The flag of Botswana has a light blue field with a white-edged black horizontal band across its center."
        },
        "coatOfArms": {
            "png": "https://mainfacts.com/media/images/coats_of_arms/bw.png",
            "svg": "https://mainfacts.com/media/images/coats_of_arms/bw.svg"
        },
        "startOfWeek": "monday",
        "capitalInfo": {
            "latlng": [
                -24.63,
                25.9
            ]
        },
        "postalCode": {
            "format": null,
            "regex": null
        }
    }
```

### Response (201 Created)
    ```
    {
        "success": "Country created successfully."
    }
    ```

# PUT /api/update-country/<cca3>/ — Update a Country
Description:
Updates the details of a specific country identified by its cca3 code. Requires authentication via token.

Authentication Required
Include your Token in the request header:

Header Example: `Authorization: Token your_token_here`

## Request
Method: PUT
URL: /api/update-country/NOR/ — Replace NOR with the actual cca3 of the country you want to update.

Headers: `Authorization: Token your_token_here`


## Request
Method: PUT
URL: /api/update-country/NOR/ — Replace NOR with the actual cca3 of the country you want to update.

Headers: 
```
Authorization: Token your_token_here
Content-Type: application/json
```

```
{
        "name": {
            "common": "Test1",
            "official": "Republic of Test",
            "nativeName": {
                "eng": {
                    "official": "Republic of Test1",
                    "common": "Botswana"
                },
                "tsn": {
                    "official": "Lefatshe la Botswana",
                    "common": "Test1"
                }
            }
        },
        "tld": [
            ".bw"
        ],
        "cca2": "Te",
        "ccn3": "072",
        "cioc": "BOT",
        "independent": true,
        "status": "officially-assigned",
        "unMember": true,
        "currencies": {
            "BWP": {
                "symbol": "P",
                "name": "Botswana pula"
            }
        },
        "idd": {
            "root": "+2",
            "suffixes": [
                "67"
            ]
        },
        "capital": [
            "Gaborone"
        ],
        "altSpellings": [
            "BW",
            "Republic of Botswana",
            "Lefatshe la Botswana"
        ],
        "region": "Africa",
        "subregion": "Southern Africa",
        "languages": {
            "eng": "English",
            "tsn": "Tswana"
        },
        "latlng": [
            -22.0,
            24.0
        ],
        "landlocked": true,
        "borders": [
            "NAM",
            "ZAF",
            "ZMB",
            "ZWE"
        ],
        "area": 582000.0,
        "demonyms": {
            "eng": {
                "f": "Motswana",
                "m": "Motswana"
            },
            "fra": {
                "f": "Botswanaise",
                "m": "Botswanais"
            }
        },
        "cca3": "TES",
        "translations": {
            "ara": {
                "official": "جمهورية بوتسوانا",
                "common": "بوتسوانا"
            },
            "bre": {
                "official": "Republik Botswana",
                "common": "Botswana"
            },
            "ces": {
                "official": "Botswanská republika",
                "common": "Botswana"
            },
            "cym": {
                "official": "Republic of Botswana",
                "common": "Botswana"
            },
            "deu": {
                "official": "Republik Botsuana",
                "common": "Botswana"
            },
            "est": {
                "official": "Botswana Vabariik",
                "common": "Botswana"
            },
            "fin": {
                "official": "Botswanan tasavalta",
                "common": "Botswana"
            },
            "fra": {
                "official": "République du Botswana",
                "common": "Botswana"
            },
            "hrv": {
                "official": "Republika Bocvana",
                "common": "Bocvana"
            },
            "hun": {
                "official": "Botswanai Köztársaság",
                "common": "Botswana"
            },
            "ind": {
                "official": "Republik Botswana",
                "common": "Botswana"
            },
            "ita": {
                "official": "Repubblica del Botswana",
                "common": "Botswana"
            },
            "jpn": {
                "official": "ボツワナ共和国",
                "common": "ボツワナ"
            },
            "kor": {
                "official": "보츠와나 공화국",
                "common": "보츠와나"
            },
            "nld": {
                "official": "Republiek Botswana",
                "common": "Botswana"
            },
            "per": {
                "official": "جمهوری بوتسوانا",
                "common": "بوتسوانا"
            },
            "pol": {
                "official": "Republika Botswany",
                "common": "Botswana"
            },
            "por": {
                "official": "República do Botswana",
                "common": "Botswana"
            },
            "rus": {
                "official": "Республика Ботсвана",
                "common": "Ботсвана"
            },
            "slk": {
                "official": "Botswanská republika",
                "common": "Botswana"
            },
            "spa": {
                "official": "República de Botswana",
                "common": "Botswana"
            },
            "srp": {
                "official": "Република Боцвана",
                "common": "Боцвана"
            },
            "swe": {
                "official": "Republiken Botswana",
                "common": "Botswana"
            },
            "tur": {
                "official": "Botsvana Cumhuriyeti",
                "common": "Botsvana"
            },
            "urd": {
                "official": "جمہوریہ بوٹسوانا",
                "common": "بوٹسوانا"
            },
            "zho": {
                "official": "博茨瓦纳共和国",
                "common": "博茨瓦纳"
            }
        },
        "flag": "🇧🇼",
        "maps": {
            "googleMaps": "https://goo.gl/maps/E364KeLy6N4JwxwQ8",
            "openStreetMaps": "https://www.openstreetmap.org/relation/1889339"
        },
        "population": 2351625,
        "gini": {
            "2015": 53.3
        },
        "fifa": "BOT",
        "car": {
            "signs": [
                "BW"
            ],
            "side": "left"
        },
        "timezones": [
            "UTC+02:00"
        ],
        "continents": [
            "Africa"
        ],
        "flags": {
            "png": "https://flagcdn.com/w320/bw.png",
            "svg": "https://flagcdn.com/bw.svg",
            "alt": "The flag of Botswana has a light blue field with a white-edged black horizontal band across its center."
        },
        "coatOfArms": {
            "png": "https://mainfacts.com/media/images/coats_of_arms/bw.png",
            "svg": "https://mainfacts.com/media/images/coats_of_arms/bw.svg"
        },
        "startOfWeek": "monday",
        "capitalInfo": {
            "latlng": [
                -24.63,
                25.9
            ]
        },
        "postalCode": {
            "format": null,
            "regex": null
        }
    }
```

### Response (200 OK):
```
{
    "success": "Country 'Test1' updated successfully."
}
```


# DELETE /api/delete-country/<cca3>/ — Delete a Country
Description: Deletes a specific country identified by its cca3 code. Requires token-based authentication.

 Authentication Required
Include your Token in the request header:
Header Example: `Authorization: Token your_token_here`


## Request
Method: DELETE
URL: /api/delete-country/NOR/ — Replace NOR with the cca3 of the country you want to delete.

Headers: `Authorization: Token your_token_here`

### Response (200 OK)
```
{
  "message": "Country 'NOR' has been deleted successfully."
}
```



# GET /api/regional-countries/<cca3>/ — Get Countries in the Same Region
Description: Fetches a list of countries that are in the same region as the country identified by the provided cca3 code.

Authentication Required
Include your Token in the request header:

Header Example: `Authorization: Token your_token_here`

## Request
Method: GET
URL: /api/regional-countries/NOR/ — Replace NOR with the cca3 code of the target country.

Headers: `Authorization: Token your_token_here`

## Response (200 OK)
```
[
  "Sweden",
  "Denmark",
  "Finland"
]
```

# GET /api/same-language/<lang_code>/ — Get Countries by Language
Description: Retrieves a list of countries where the specified language (by language code) is spoken.

Authentication Required
Include your Token in the request header:

Header Example: `Authorization: Token your_token_here`

## Request
Method: GET
URL: /api/same-language/eng/ — Replace eng with the desired language code (e.g., spa, fra, deu).

Headers: `Authorization: Token your_token_her`

### Response (200 OK)
```
[
  "United Kingdom",
  "United States",
  "Canada"
]
```


# GET /api/countries/search/?search=<query> — Search Countries by Name
Description: Search for countries by name. Supports partial matching, case-insensitive.

🔐 Authentication Required
Include your Token in the request header:

Header Example: `Authorization: Token your_token_here`

## Request
Method: GET
URL Example: /countries/search/?search=land

Query Parameters:

search: A partial or full string to match against country names.

Headers: `Authorization: Token your_token_here`
