def greet_user(name: str, age: int) -> str:
    if age < 0:
        return "Invalid age"
    return f"Hello, {name}! You are {age} years old."