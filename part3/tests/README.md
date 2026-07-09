# HBnB API — Testing Report

## Overview
This document describes the testing performed on the HBnB API endpoints for
Part 2. Two methods were used: automated unit tests with Python's `unittest`
and Flask's test client (`tests/test_endpoints.py`), and manual black-box
testing with cURL and the Swagger UI at `/api/v1/`.

## Running the automated tests
From the project root:

    python3 -m unittest discover

## Validation rules verified
- User: first and last name required (max 50 chars); valid email format.
- Amenity: name required (max 50 chars).
- Place: title required; price positive; latitude in [-90, 90];
  longitude in [-180, 180]; owner must exist.
- Review: text required; rating between 1 and 5; user and place must exist.

## Test cases

### Users
| Case | Input | Expected | Result |
|------|-------|----------|--------|
| Valid user | valid data | 201 | Pass |
| Invalid email | "not-an-email" | 400 | Pass |
| Empty first name | "" | 400 | Pass |
| Unknown id (GET) | random id | 404 | Pass |

### Amenities
| Case | Input | Expected | Result |
|------|-------|----------|--------|
| Valid amenity | name "Wifi" | 201 | Pass |
| Empty name | "" | 400 | Pass |

### Places
| Case | Input | Expected | Result |
|------|-------|----------|--------|
| Valid place | valid data + real owner | 201 | Pass |
| Unknown owner | owner_id "nobody" | 400 | Pass |
| Negative price | price -50 | 400 | Pass |
| Latitude out of range | 200 | 400 | Pass |

### Reviews
| Case | Input | Expected | Result |
|------|-------|----------|--------|
| Valid review | valid data | 201 | Pass |
| Rating above 5 | rating 6 | 400 | Pass |
| Delete review | existing id | 200 | Pass |

## Manual testing
Each endpoint was also exercised through the Swagger UI (`/api/v1/`) and with
cURL. Example:

    curl -X POST http://127.0.0.1:5000/api/v1/users/ \
      -H "Content-Type: application/json" \
      -d '{"first_name":"Karen","last_name":"Navarro","email":"k@test.com"}'

All responses matched the expected status codes and JSON formats.
