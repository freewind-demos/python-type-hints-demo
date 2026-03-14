# Python 类型提示

def greet(name: str) -> str:
    return f"Hello, {name}!"

def process(items: list[int]) -> dict[str, int]:
    return {"count": len(items)}

from typing import Optional, Union, List, Dict

def find_user(user_id: int, name: Optional[str] = None) -> Union[str, None]:
    return name or "未找到"

# 泛型
from typing import TypeVar, Generic

T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value: T = value

box: Box[int] = Box(42)
