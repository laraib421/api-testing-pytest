"""JSON schemas used for contract validation."""

POST_SCHEMA = {
    "type": "object",
    "required": ["userId", "id", "title", "body"],
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
}

USER_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "username", "email", "address", "company"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string", "pattern": "^[^@\\s]+@[^@\\s]+$"},
        "address": {"type": "object"},
        "company": {"type": "object"},
    },
}
