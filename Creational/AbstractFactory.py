from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self, num=1):
        product = self.factory_method(num)
        return f"Creator: The same creator's code has worked with {product.operation()}"


class Product(ABC):
    @abstractmethod
    def operation(self):
        pass


class ItalyFood(Creator):
    def factory_method(self, num) -> Product:
        match num:
            case 1:
                return Pizza()
            case 2:
                return Pasta()
            case _:
                raise ImportError("Непонятно что")


class Pizza(Product):
    def operation(self):
        return f"First result"


class Pasta(Product):
    def operation(self):
        return f"Second result"



class AsiaFood(Creator):
    def factory_method(self, num) -> Product:
        match num:
            case 1:
                return Sushi()
            case 2:
                return Wok()
            case _:
                raise ImportError("Непонятно что")


class Sushi(Product):
    def operation(self):
        return f"First Sushi"


class Wok(Product):
    def operation(self):
        return f"Second Wok"


class AbstractFactory:
    def factory_method(self, num):
        match num:
            case 1:
                return ItalyFood
            case 2:
                return AsiaFood
            case _:
                raise ImportError("Непонятно что")


if __name__ == "__main__":
    print(AbstractFactory().factory_method(2)().some_operation(1))