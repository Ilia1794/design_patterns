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


class ConcreteCreator(Creator):
    def factory_method(self, num) -> Product:
        match num:
            case 1:
                return ConcreteProduct()
            case 2:
                return ConcreteProduct2()
            case _:
                raise ImportError("Непонятно что")


class ConcreteProduct(Product):
    def operation(self):
        return f"First result"


class ConcreteProduct2(Product):
    def operation(self):
        return f"Second result"


if __name__ == "__main__":
    print(ConcreteCreator().some_operation(2))
