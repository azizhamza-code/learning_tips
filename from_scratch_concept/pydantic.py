from typing import Any, Dict, Type

class ValidationError(Exception):
    pass

class BaseModel:
    def __init__(self, **kwargs):
        for field_name, field_type in self.__annotations__.items():
            if field_name not in kwargs:
                raise ValidationError(f"Missing field: {field_name}")
            value = kwargs[field_name]
            if not isinstance(value, field_type):
                raise ValidationError(f"Field {field_name} must be of type {field_type.__name__}")
            setattr(self, field_name, value)
    
    def dict(self) -> Dict[str, Any]:
        return {field: getattr(self, field) for field in self.__annotations__}

class User(BaseModel):
    id: int
    name: str
    age: int

try:
    user = User(id=1, name="John Doe", age=30)
    print(user.dict())
except ValidationError as e:
    print(e)

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int

try:
    user = User(id=1, name="John Doe", age=30)
    print(user.dict())
except ValidationError as e:
    print(e)

# Output:
# {'id': 1, 'name': 'John Doe', 'age': 30}
# {'id': 1, 'name': 'John Doe', 'age': 30}
