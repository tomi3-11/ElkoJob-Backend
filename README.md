# ElkoJob-Backend API Documentation for Frontend

This document provides all necessary details for integrating with the **Candidates & Jobs API**. It includes endpoints for candidate profiles, job listings, and job applications.

---


# 1. Authentication API Endpoints

**Base URL:** `/api/auth/`

All endpoints require JWT authentication.

**Header (all requests):**
```

Authorization: Bearer <ACCESS_TOKEN>
Content-Type: application/json

```
---

### 1. User Registration

| Method | Endpoint              | Description                          | Request Body                                                                                                                                     |
| ------ | --------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| POST   | `/auth/registration/` | Register a new user                  | `json { "username": "string", "email": "string", "password1": "string", "password2": "string", "first_name": "string", "last_name": "string" } ` |
| GET    | `/auth/registration/` | List registration options (optional) | N/A                                                                                                                                              |

**Response Example:**

```json
{
  "key": "access_token",
  "user": {
    "pk": 1,
    "username": "alice2025",
    "email": "alice2025@gmail.com",
    "first_name": "Alice",
    "last_name": "Johnson"
  }
}
```

---

### 2. Login

| Method | Endpoint       | Description                                           | Request Body                                           |
| ------ | -------------- | ----------------------------------------------------- | ------------------------------------------------------ |
| POST   | `/auth/login/` | Log in an existing user and get access/refresh tokens | `json { "username": "string", "password": "string" } ` |

**Response Example:**

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token",
  "user": {
    "pk": 1,
    "username": "alice2025",
    "email": "alice2025@gmail.com",
    "first_name": "Alice",
    "last_name": "Johnson"
  }
}
```

---

### 3. Logout

| Method | Endpoint        | Description                       | Request Body |
| ------ | --------------- | --------------------------------- | ------------ |
| POST   | `/auth/logout/` | Log out user and invalidate token | N/A          |

---

### 4. Password Reset

| Method | Endpoint                        | Description                       | Request Body                                                                                        |
| ------ | ------------------------------- | --------------------------------- | --------------------------------------------------------------------------------------------------- |
| POST   | `/auth/password/reset/`         | Request password reset email      | `json { "email": "user@example.com" } `                                                             |
| POST   | `/auth/password/reset/confirm/` | Confirm password reset with token | `json { "uid": "uidb64", "token": "token", "new_password1": "string", "new_password2": "string" } ` |

---

### 5. Password Change

| Method | Endpoint                 | Description                     | Request Body                                                                               |
| ------ | ------------------------ | ------------------------------- | ------------------------------------------------------------------------------------------ |
| POST   | `/auth/password/change/` | Change password while logged in | `json { "old_password": "string", "new_password1": "string", "new_password2": "string" } ` |

---

### 6. Token Refresh

| Method | Endpoint               | Description              | Request Body                           |
| ------ | ---------------------- | ------------------------ | -------------------------------------- |
| POST   | `/auth/token/refresh/` | Refresh JWT access token | `json { "refresh": "refresh_token" } ` |

---

### 7. Token Verify

| Method | Endpoint              | Description              | Request Body                            |
| ------ | --------------------- | ------------------------ | --------------------------------------- |
| POST   | `/auth/token/verify/` | Verify validity of a JWT | `json { "token": "jwt_access_token" } ` |

---

### 8. Email Verification / Confirmation

| Method | Endpoint                           | Description                               | Request Body                                     |
| ------ | ---------------------------------- | ----------------------------------------- | ------------------------------------------------ |
| POST   | `/auth/registration/verify-email/` | Confirm a user’s email after registration | `json { "key": "confirmation_key_from_email" } ` |

**Notes:**

* `confirmation_key_from_email` comes from the email sent by allauth.
* In **development**, if using `EMAIL_BACKEND = console`, the key is printed in the console.

---

## 2. Candidate Profile

**Base URL:** `/api/candidates/profile/`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/candidates/profile/` | Retrieve the logged-in candidate's profile |
| PUT    | `/api/candidates/profile/` | Update the entire profile (skills, bio, resume) |
| PATCH  | `/api/candidates/profile/` | Update a part of the profile |

**Profile Fields:**
```json
{
  "skills": "string",
  "bio": "string",
  "resume": "file or null",
  "subscription_active": "boolean"
}
```

---

## 2. Jobs

**Base URL:** `/api/candidates/jobs/`

| Method | Endpoint                | Description                                   |
| ------ | ----------------------- | --------------------------------------------- |
| GET    | `/api/candidates/jobs/` | List all available jobs with optional filters |

**Query Parameters (all optional):**

* `type`: Full-time, Contract
* `level`: Internship, Senior
* `country`: e.g., Kenya
* `city`: e.g., Nairobi
* `work_type`: Remote, Hybrid
* `salary_range`: e.g., 0-100k
* `category`: Engineering, etc.

**Example GET with filters:**

```
GET /api/candidates/jobs/?country=Kenya&level=Internship
```

**Job Fields:**

```json
{
    "title": "string",
    "type": "string",
    "level": "string",
    "country": "string",
    "city": "string",
    "work_type": "string",
    "salary_range": "string",
    "category": "string"
}
```

---

## 3. Job Application

**Base URL:** `/api/candidates/jobs/<job_id>/apply/`

| Method | Endpoint                               | Description                                             |
| ------ | -------------------------------------- | ------------------------------------------------------- |
| POST   | `/api/candidates/jobs/<job_id>/apply/` | Apply for a specific job (requires active subscription) |

**Request Body:**

```json
{}
```

**Response Fields:**

```json
{
  "id": 1,
  "status": "applied",
  "applied_at": "timestamp"
}
```

**Error Responses:**

* `Active subscription required to apply` → If candidate has no active subscription
* `Already applied` → If candidate already applied to the same job

---

## 4. Testing

* Use JWT in `Authorization` header for all endpoints.
* Candidate profile updates reflect immediately in the database.
* Jobs support filtering via query parameters.
* Job application requires active subscription.

---

## 5. Notes for Frontend

1. Use the `/api/auth/login/` endpoint to obtain `access` token for API requests.
2. All endpoints return JSON.
3. Profile, jobs, and applications are linked to the logged-in user via JWT.
<!-- 4. File uploads (resume) should be sent as `multipart/form-data` if implemented. -->
4. For search/filtering, append query parameters as needed.

