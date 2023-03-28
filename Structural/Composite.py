from abc import ABC, abstractmethod


class Unit(ABC):
    """
    Абстрактный компонент, в данном случае это - отряд (отряд может
    состоять из одного солдата или более)
    """

    @abstractmethod
    def print(self) -> None:
        """
        Вывод данных о компоненте
        """
        pass


class Archer(Unit):
    """
    Лучник
    """

    def print(self) -> None:
        print('лучник', end=' ')


class Knight(Unit):
    """
    Рыцарь
    """

    def print(self) -> None:
        print('рыцарь', end=' ')


class Swordsman(Unit):
    """
    Мечник
    """

    def print(self) -> None:
        print('мечник', end=' ')


class Squad(Unit):
    """
    Компоновщик - отряд, состоящий более чем из одного человека. Также
    может включать в себя другие отряды-компоновщики.
    """

    def __init__(self):
        self._units = []

    def print(self) -> None:
        print("Отряд {} (".format(self.__hash__()), end=' ')
        for u in self._units:
            u.print()
        print(')')

    def add(self, unit: Unit) -> None:
        """
        Добавление нового отряда
        
        :param unit: отряд (может быть как базовым, так и компоновщиком)
        """
        self._units.append(unit)
        unit.print()
        print('присоединился к отряду {}'.format(self.__hash__()))
        print()

    def remove(self, unit: Unit) -> None:
        """
        Удаление отряда из текущего компоновщика
        
        :param unit: объект отряда
        """
        for u in self._units:
            if u == unit:
                self._units.remove(u)
                u.print()
                print('покинул отряд {}'.format(self.__hash__()))
                print()
                break
        else:
            unit.print()
            print('в отряде {} не найден'.format(self.__hash__()))
            print()


if __name__ == '__main__':
    print('OUTPUT:')
    squad = Squad()
    squad.add(Knight())
    squad.add(Knight())
    squad.add(Archer())
    swordsman = Swordsman()
    squad.add(swordsman)
    squad.remove(swordsman)
    squad.print()
    squad_big = Squad()
    squad_big.add(Swordsman())
    squad_big.add(Swordsman())
    squad_big.add(squad)
    squad_big.print()