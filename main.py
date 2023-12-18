import copy
import inspect
from typing import Callable, Any, List, Type


class ColoService:
    def __init__(self):
        self.colors = {
            'grey': "\x1b[38;20m",
            'yellow': "\x1b[33;20m",
            'red': "\x1b[31;20m",
            'bold_red': "\x1b[31;1m",
        }

    def rize(self, text, color):
        return f"{self.colors[color]}{text}\x1b[0m"


class DictService:
    def __init__(self):
        self.data = {}

        for name, method in inspect.getmembers(self, predicate=inspect.ismethod):
            if not name.startswith('__') and name in self.data:
                self.data[name] = method

    def __getattr__(self, name):
        colo = ColoService()

        if name in self.__dict__:
            return self.__dict__[name]
        else:
            def error_handler():
                print(
                    f"[{colo.rize('DictService:Warning', 'yellow')}] [\n"
                    f"  def[{colo.rize(name, 'red')}](...?): does not exist in dictionary"
                    "\n]"
                )  # TODO : Error handler class.

            return error_handler

    def lava1(self) -> print:
        print('lava1' or self)

    def lava2(self) -> print:
        print('lava2' or self)


class MetatableService:
    def __init__(self):
        self.backup = {}

    def new(self, __class: Type[Any] = None, __dict: {Any} = None) -> Callable[[Any], None] or None:
        colo = ColoService()

        if not isinstance(__class, type) or not isinstance(__dict, dict):
            print(
                f"[{colo.rize('MetatableService:Error', 'red')}] [\n"
                f"  {colo.rize('param: __class:List[] or array:[] is missing', 'red')}"
                "\n]"
            )  # TODO : Error handler class
            return None

        __data = __class()
        __metatable = copy.deepcopy(__dict)

        def __metatable_add(cls, key, value):
            cls.data[key] = value

        def __iter__(cls):
            return iter(cls.data.items())

        setattr(__data, '__iter__', __iter__.__get__(__data))
        setattr(__data, '__metatable_add', __metatable_add.__get__(__data))

        __data.__iter__ = __iter__
        __data.__metatable_add = __metatable_add

        for key, value in __metatable.items():
            __data.__metatable_add(__data, key, value)

        return __data or self.backup


# Services
metatable = MetatableService()  # Merge any array together with any class.
functions = DictService()  # -- Work's as intended, just simple error handling.


class testMeta:
    def __init__(self):
        self.data = {
            'IamTestMetaTestData': True
        }

    def new(self):
        for key, value in self.data.items():
            print(key, value)


# my weird debugging method
Testing_MetatableService = True
Testing_DictService = False


if __name__ == '__main__':
    if Testing_MetatableService and not Testing_DictService:
        test = metatable.new(testMeta, {
            'HasPrivileges': True,
            'TestArray': [],
        })

        test.new()
    elif Testing_DictService:
        functions.lava2()
        functions.lava7()
