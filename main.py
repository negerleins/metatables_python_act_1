import copy
import inspect


class ColoService:
    def __init__(self):
        self.data = {}
        self.colors = {
            'grey': "\x1b[38;20m",
            'yellow': "\x1b[33;20m",
            'red': "\x1b[31;20m",
            'bold_red': "\x1b[31;1m",
        }

    def rize(self, text, color):
        return f"{self.colors[color]}{text}\x1b[0m"


colo = ColoService()


class DictService:
    def __init__(self):
        self.data = {}

        for name, method in inspect.getmembers(self, predicate=inspect.ismethod):
            if not name.startswith('__') and name in self.data:
                self.data[name] = method

    def __getattr__(self, name):
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


class SharedService:
    def __init__(self):
        self.metatables = {}
        self.dict = DictService()


class MetatableService:
    def __init__(self):
        self.dict = DictService()

    def create(self, shared_instance):
        for key, value in shared_instance.dict.data.items():
            self.dict.data[key] = copy.deepcopy(value)

    def new(self, name):
        new_metatable = MetatableService() or self  # To satisfy static warning(s).
        new_metatable.create(shared)
        return new_metatable.dict


# Services
shared = SharedService()
shared.dict = DictService()
metatable = MetatableService()


if __name__ == '__main__':
    test = metatable.new('project1')
    test.lava2()
    test.lava5()
