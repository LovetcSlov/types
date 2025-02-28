from typing import List, Dict, TypedDict, Protocol

def add(x: int, y: int) -> int:
    """Returns the sum of two integers."""
    return x + y

print(add(3, 5))  # 8

# Пример использования аннотаций для списка и словаря
def process_numbers(numbers: List[int]) -> Dict[str, int]:
    """Returns a dictionary with the sum and max of a list of numbers."""
    return {"sum": sum(numbers), "max": max(numbers)}

print(process_numbers([1, 2, 3, 4]))  # {'sum': 10, 'max': 4}

# Использование TypedDict для строгих типов в словаре
class User(TypedDict):
    name: str
    age: int

def get_user_info(user: User) -> str:
    """Returns user information as a formatted string."""
    return f"User {user['name']} is {user['age']} years old."

print(get_user_info({"name": "Alice", "age": 30}))  # User Alice is 30 years old.

# Пример использования Protocol
def square(n: int) -> int:
    return n * n

class CallableFunction(Protocol):
    def __call__(self, x: int) -> int: ...

def apply_func(func: CallableFunction, value: int) -> int:
    return func(value)

print(apply_func(square, 4))  # 16