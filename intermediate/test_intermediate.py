# await
#from collections.abc import Awaitable
#
#
#def run_async(func: Awaitable[int]): ...


## End of your code ##
# from asyncio import Queue
#
# queue: Queue[int] = Queue()
# queue2: Queue[str] = Queue()
#
#
# async def async_function() -> int:
#    return await queue.get()
#
#
# async def async_function2() -> str:
#    return await queue2.get()
#
#
# run_async(async_function())
# run_async(1)  # expect-type-error
# run_async(async_function2())  # expect-type-error

# Callable

# from typing import Callable, TypeAlias
#
## Определяем тип SingleStringInput с использованием TypeAlias
# SingleStringInput: TypeAlias = Callable[[str], None]

# class-var

# from typing import ClassVar
#
# class Foo:
#    bar: ClassVar[int]


#decorator
#def decorator[T: Callable](func: T) -> T:
#    return func
#
#
### End of your code ##
#@decorator
#def foo(a: int, *, b: str) -> None:
#    ...
#
#
#@decorator
#def bar(c: int, d: str) -> None:
#    ...
#
#
#foo(1, b="2")
#bar(c=1, d="2")
#
#foo(1, "2")  # expect-type-error
#foo(a=1, e="2")  # expect-type-error
#decorator(1)  # expect-type-error


#empty-tuple
#def foo(x: tuple[()]):
#    pass
#
#
### End of your code ##
#foo(())
#foo((1,))  # expect-type-error


#generic
#def add[T](a: T, b: T) -> T:
#    ...
#
#
### End of your code ##
#from typing import List, assert_type
#
#assert_type(add(1, 2), int)
#assert_type(add("1", "2"), str)
#assert_type(add(["1"], ["2"]), List[str])
#assert_type(add(1, "2"), int)  # expect-type-error

#generic2
#def add[T: (str, int)](a: T, b: T) -> T:
#    ...
#
#
### End of your code ##
#from typing import assert_type
#
#assert_type(add(1, 2), int)
#assert_type(add("1", "2"), str)
#
#add(["1"], ["2"])  # expect-type-error
#add("1", 2)  # expect-type-error

#generic3
#def add[T: int](a: T) -> T:
#    ...
#
#
### End of your code ##
#from typing import assert_type
#
#
#class MyInt(int):
#    pass
#
#
#assert_type(add(1), int)
#assert_type(add(MyInt(1)), MyInt)
#assert_type(add("1"), str)  # expect-type-error
#add(["1"], ["2"])  # expect-type-error
#add("1", 2)  # expect-type-error

#instance-var
#class Foo:
#    bar: int

#literal
#from typing import Literal
#
#
#def foo(direction: Literal["left", "right"]):
#    ...
#
#
### End of your code ##
#foo("left")
#foo("right")
#
#a = "".join(["l", "e", "f", "t"])
#foo(a)  # expect-type-error


#literalstring
#from typing import LiteralString, Iterable, Any, List, Dict, Union
#
#def execute_query(sql: LiteralString, parameters: Iterable[Union[str, int, float]] = ()) -> List[Dict[str, Any]]:
#    """
#    Выполняет SQL-запрос с использованием параметров для предотвращения SQL-инъекций.
#
#    :param sql: SQL-запрос в виде строки.
#    :param parameters: Итерируемый объект с параметрами.
#    :return: Результат выполнения запроса (список словарей).
#def query_user(user_id: str):
#    query = f"SELECT * FROM data WHERE user_id = {user_id}"
#    execute_query(query)  # expect-type-error
#def query_data(user_id: str, limit: bool) -> None:
#    query = """
#        SELECT
#            user.name,
#            user.age
#        FROM data
#        WHERE user_id = ?
#    if limit:
#        query += " LIMIT 1"
#
#    execute_query(query, (user_id,))



#self
#from typing import Self
#
#
#class Foo:
#    def return_self(self) -> Self:
#        ...
#class SubclassOfFoo(Foo):
#    pass
#
#
#f: Foo = Foo().return_self()
#sf: SubclassOfFoo = SubclassOfFoo().return_self()
#
#sf: SubclassOfFoo = Foo().return_self()  # expect-type-error



#typed-dict
#from typing import TypedDict
#
#
#class Student(TypedDict):
#    name: str
#    age: int
#    school: str
#
#
## Alternatively you can write:
## Student = TypedDict('Student', {'name': str, 'age': int, 'school': str})
#
#
### End of your code ##
#a: Student = {"name": "Tom", "age": 15, "school": "Hogwarts"}
#a: Student = {"name": 1, "age": 15, "school": "Hogwarts"}  # expect-type-error
#a: Student = {(1,): "Tom", "age": 2, "school": "Hogwarts"}  # expect-type-error
#a: Student = {"name": "Tom", "age": "2", "school": "Hogwarts"}  # expect-type-error
#a: Student = {"name": "Tom", "age": 2}  # expect-type-error
#assert Student(name="Tom", age=15, school="Hogwarts") == dict(
#    name="Tom", age=15, school="Hogwarts"
#)


#typed-dict2
#
#from typing import TypedDict, NotRequired
#
#
#class Student(TypedDict):
#    name: str
#    age: int
#    school: NotRequired[str]
#
#a: Student = {"name": "Tom", "age": 15}
#a: Student = {"name": "Tom", "age": 15, "school": "Hogwarts"}
#a: Student = {"name": 1, "age": 15, "school": "Hogwarts"}  # expect-type-error
#a: Student = {(1,): "Tom", "age": 2, "school": "Hogwarts"}  # expect-type-error
#a: Student = {"name": "Tom", "age": "2", "school": "Hogwarts"}  # expect-type-error
#a: Student = {"z": "Tom", "age": 2}  # expect-type-error
#assert Student(name="Tom", age=15) == dict(name="Tom", age=15)
#assert Student(name="Tom", age=15, school="Hogwarts") == dict(
#    name="Tom", age=15, school="Hogwarts"
#)


#typed-dict2
#
#from typing import TypedDict, Required
#
#
#class Person(TypedDict, total=False):
#    name: Required[str]
#    age: int
#    gender: str
#    address: str
#    email: str
#
#    a: Person = {
#    "name": "Capy",
#    "age": 1,
#    "gender": "Male",
#    "address": "earth",
#    "email": "capy@bara.com",
#}
#a: Person = {"name": "Capy"}
## fmt: off
#a: Person = {"age": 1, "gender": "Male", "address": "", "email": ""} # expect-type-error


#unpack

from typing import Unpack, TypedDict


class Person(TypedDict):
    name: str
    age: int


#def foo(**kwargs: Unpack[Person]):
#    ...
#
#person: Person = {"name": "The Meaning of Life", "age": 1983}
#foo(**person)
#foo(**{"name": "Brian", "age": 30})
#
#foo(**{"name": "Brian"})  # expect-type-error
#person2: dict[str, object] = {"name": "Brian", "age": 20}
#foo(**person2)  # expect-type-error
#foo(**{"name": "Brian", "age": "1979"})  # expect-type-error