# HBnB Evolution — Sequence Diagrams for API Calls

## 1. User Registration

```mermaid
sequenceDiagram
    participant User
    participant API
    participant Facade
    participant UserModel
    participant Database

    User->>API: POST /users (registration data)
    API->>Facade: create_user(data)
    Facade->>UserModel: validate and create User
    UserModel-->>Facade: User object (or error)
    Facade->>Database: save(user)
    Database-->>Facade: confirm save
    Facade-->>API: return created User
    API-->>User: 201 Created (user JSON)
```

## 2. Place Creation

```mermaid
sequenceDiagram
    participant User
    participant API
    participant Facade
    participant PlaceModel
    participant Database

    User->>API: POST /places (place data)
    API->>Facade: create_place(data)
    Facade->>PlaceModel: validate and create Place
    PlaceModel-->>Facade: Place object (or error)
    Facade->>Database: save(place)
    Database-->>Facade: confirm save
    Facade-->>API: return created Place
    API-->>User: 201 Created (place JSON)
```

## 3. Review Submission

```mermaid
sequenceDiagram
    participant User
    participant API
    participant Facade
    participant ReviewModel
    participant Database

    User->>API: POST /places/{id}/reviews (review data)
    API->>Facade: create_review(place_id, data)
    Facade->>Database: get place by id
    Database-->>Facade: place (or not found)
    Facade->>ReviewModel: validate and create Review
    ReviewModel-->>Facade: Review object (or error)
    Facade->>Database: save(review)
    Database-->>Facade: confirm save
    Facade-->>API: return created Review
    API-->>User: 201 Created (review JSON)
```

## 4. Fetching a List of Places

```mermaid
sequenceDiagram
    participant User
    participant API
    participant Facade
    participant Database

    User->>API: GET /places (filter criteria)
    API->>Facade: get_places(filters)
    Facade->>Database: query places matching filters
    Database-->>Facade: list of places
    Facade-->>API: return list of places
    API-->>User: 200 OK (places JSON array)
```

## Explanatory Notes

### 1. User Registration
When the account is created the API receives the request to signup and it sends it through the facade using the User model. It validates the data, builds the object and then saves it.

### 2. Place Creation
  This is where the user creates a new property listing, the facade validates and then creates the Place through the model. Linked to its owner from the authenticated user request. 

### 3. Review Submission
When a user leaves a review, the facade first checks the target place actually exists, because a review cannot be written for something that is not there. Once it validates the existence, it creates the Review, saves it and returns it. 

### 4. Fetching a List of Places
A user sends a request for a place, the facade looks into the persistence layer, and brings a collection back. 

### Flow Across All Diagrams
Every diagram follows the same path down through the layers — API to Facade to Model/Database — and back up, with the facade acting as the single coordinator between the presentation layer and the deeper layers.