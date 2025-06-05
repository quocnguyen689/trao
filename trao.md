## Danh sách bảng
## Lược đồ quan hệ giữa các bảng

### 1. Collections

| Column Name       | Data Type      |
|-------------------|----------------|
| id                | int            |
| name              | string         |
| icon_url          | string         |
| created_date      | datetime       |

### 2. Ads

| Column Name       | Data Type           | Note |
|------------------|---------------------|----------------|
| id               | int                 |
| ad_id            | int                 |
| list_id          | int                 |
| collection_id    | int                 | FK to Collections.id |
| name             | string              |
| price            | number              |
| category_name    | character varying   |
| area_name        | character varying   |
| region_name      | character varying   |
| type             | string              | Values: sell, gift, exchange |
| short_description| string              |
| description      | string              |
| image_url        | string              |
| seller_id        | int                 | FK to Users.id |
| longitude        | number              |
| latitude         | number              |
| location         | number              |
| status           | string              | Values: active, draft, expired |
| created_date     | datetime            |

### 3. UserActivities

| Column Name       | Data Type      | Note |
|-------------------|----------------|----------------|
| id                | int            |
| ad_id             | int            | FK to Ads.id |
| user_id           | int            | FK to Users.id |
| action_type       | string         | Values: like |
| created_date      | datetime       |

### 4. Offers

| Column Name       | Data Type      | Note |
|-------------------|----------------|----------------|
| id                | int            |
| ad_id             | int            | FK to Ads.id |
| owner_id          | int            | FK to Users.id |
| status            | string         | Values: new, accepted, rejected, cancelled |
| created_date      | datetime       |

### 5. Users

| Column Name       | Data Type      | Note |
|-------------------|----------------|----------------|
| id                | int            |
| name              | string         |
| type              | string         | Values: seller, buyer |
| created_date      | datetime       |

### Lược đồ quan hệ

- **Collections** (1) <--- (N) **Ads**
- **Users** (1) <--- (N) **Ads**
- **Users** (1) <--- (N) **UserActivities**
- **Ads** (1) <--- (N) **UserActivities**
- **Ads** (1) <--- (N) **Offers**
- **Users** (1) <--- (N) **Offers**



## Danh sách API

### 1. Lấy danh sách collection
- **Endpoint:** `/api/v1/collection`
- **Method:** `GET`
- **Response:** Mảng dữ liệu chứa các trường:
    ```json
    {
        "success": true,
        "data": [
            {
                "id": "string",
                "name": "string",
                "icon_url": "string",
                "total_number_ads": "number"
            }
        ]
    }
    ```

### 2. Lấy thông tin chi tiết của quảng cáo đầu tiên trong collection
- **Endpoint:** `/api/v1/ads/first?collection_id=123`
- **Method:** `GET`
- **Request:** 
    - `collection_id`
- **Response:** Thông tin của quảng cáo đầu tiên:
    ```json
    {
        "success": true,
        "data": {
            "id": "string",
            "ad_id": "string",
            "list_id": "string",
            "name": "string",
            "short_description": "string",
            "description": "string",
            "image_url": "string",
            "seller_name": "string",
            "location_distance": "number",
            "total_offers": "number",
            "offers": [
                {
                    "id": "string",
                    "ad_name": "string",
                    "owner_name": "string",
                    "created_date": "string",
                    "status": "string"
                }
            ]
        }
    }
    ```

### 3. Lấy thông tin chi tiết của Ads tiếp theo trong collection
- **Endpoint:** `/api/v1/ads/next?collection_id=123&current_index=0`
- **Method:** `GET`
- **Request:** 
    - `collection_id`
    - `current_index`
- **Response:** Thông tin của ads:
    ```json
    {
        "success": true,
        "data": {
            "id": "string",
            "name": "string",
            "short_description": "string",
            "description": "string",
            "image_url": "string",
            "seller_name": "string",
            "location_distance": "number",
            "total_offers": "number",
            "offers": [
                {
                    "id": "string",
                    "ad_id": "int",
                    "ad_name": "string",
                    "owner_id": "int",
                    "owner_name": "string",
                    "created_date": "string",
                    "status": "string"
                }
            ]
        }
    }
    ```

### 4. API lưu quảng cáo khi nhấn nút thích
- **Endpoint:** `/api/v1/ads/heart`
- **Method:** `POST`
- **Request:**
    - `user_id`
    - `ad_id`
- **Response:**
    ```json
    {
        "success": true,
        "data": {}
    }
    ```

### 5. API cho seller cập nhật status của offer
- **Endpoint**: `/api/v1/offer/status-update`
- **Method**: `PUT`
- **Request**:
    ```json
    {
        "ad_id": "string",
        "user_id": "int",
        "action_type": "string"
    }
    ```
- **Response:**
    ```json
    {
        "success": true,
        "data": {}
    }
    ```

### 6. API tạo Ads (có thời gian thì làm)
- **Endpoint**: `/api/v1/ads`
- **Method**: `POST`
- **Request**:
    ```json
    {
        "name": "string",
        "short_description": "string",
        "description": "string",
        "image_url": "string",
        "seller_name": "string",
        "location_distance": "number",
        "total_offers": "number"
    }
    ```
- **Response**:
    ```json
    {
        "success": true,
        "data": 
        {
            "id": "string",
            "name": "string",
            "short_description": "string",
            "description": "string",
            "image_url": "string",
            "seller_name": "string",
            "location_distance": "number",
            "total_offers": "number"
        }
    }
    ``` 

### 6. API lấy danh sách ads theo user
- **Page**: Choose ads to swap
- **Description**: Chỉ lấy danh sách ads active
- **Endpoint**: `/api/v1/ads?user_id=123`
- **Method**: `GET`
- **Request**:
    - `user_id`
- **Response**:
    ```json
    {
        "success": true,
        "data": [
            {
                "id": "string",
                "name": "string",
                "short_description": "string",
                "description": "string",
                "image_url": "string",
                "seller_name": "string",
                "location_distance": "number",
                "total_offers": "number"
            }
        ]
    }
    ``` 

### 7. API tạo offer
- **Page**: Choose ads to swap
- **Endpoint**: `/api/v1/offer`
- **Method**: `POST`
- **Request**:
    ```json
    {
        "ad_id": "int",
        "owner_id": "int",
        "created_date": "datetime",
        "status": "string"
    }
    ```
- **Response**:
    ```json
    {
        "success": true,
        "data": 
        {
            "id": "int",
            "ad_id": "int",
            "owner_id": "int",
            "created_date": "datetime",
            "status": "string"
        }
    }
    ``` 