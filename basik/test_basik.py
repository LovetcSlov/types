# any
# def foo(arg):  # Функция принимает ровно один аргумент
#    pass
#
# foo(1, 2)  # expect-type-error: вызовет ошибку, так как передано два аргумента
# foo(1)     # Корректный вызов
# foo("10")  # Корректный вызов

# dict
# def foo(x: dict[str, str]): #реально ошибки не возникает, но тренажёр считает, что всё ок
#    pass
#
# foo({"foo": "bar"})
# foo({"foo": 1}) #expect-type-error

# Final
#from typing import Final
#
#my_list: Final = []

#kwargs
#def foo(**kwargs: int | str):
#    pass
#foo(a=1, b="2")
#foo(a=[1]) # expecttype-error

#list
#def foo(x: list[str]):
#    pass
#foo(["foo", "bar"])
#foo(["foo", 1]) #expect-type-error

#optional

#def foo(x: int | None = 10):
#    pass
#foo(10)
#foo(None)
#foo()
#foo("10") # expect-typeerror

#parameter

#def foo(x: int):
#    pass
#foo(10)
#foo("10") # expect-typeerror

#return
#def foo() -> int:
#    return 1
#from typing import assert_type
#assert_type(foo(), int)
#assert_type(foo(), str) # expect-type-error

#tuple
#def foo(x: tuple[str, int]):
#    pass
#foo(("foo", 1))
#foo((1, 2)) # expecttype-error
#foo(("foo", "bar")) #expect-type-error
#foo((1, "foo")) #expect-type-error

#tupealias

#type Vector = list[float]
#def foo(v: Vector):
#    pass
#foo([1.1, 2])
#foo(1)  # expect-type-error
#foo(["1"])  # expect-type-error

#union
#def foo(x: str | int):
#    pass

#variable
from typing import Any

a: int
