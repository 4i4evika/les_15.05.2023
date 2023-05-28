### 1. Создайте реализацию паттерна Builder. Протестируйте работу созданного класса.

# class Car():
# 	def __init__(self):
# 		self.name = None
# 		self.engine = None
# 		self.tyres = None
# 		self.speedometer = None
#
# 	def __str__(self):
# 		return '{} | {} | {} | {}'.format(self.name, self.engine, self.tyres, self.speedometer)
#
#
# class AbstractBuilder():
# 	def __init__(self):
# 		self.car = None
#
# 	def createNewCar(self):
# 		self.car = Car()
#
#
# class ConcreteBuilder(AbstractBuilder):
# 	def addName(self):
# 		self.car.name = "HONDA"
#
# 	def addEngine(self):
# 		self.car.engine = "4-stroke"
#
# 	def addTyres(self):
# 		self.car.tyres = "MRF"
#
# 	def addSpeedometer(self):
# 		self.car.speedometer = "0-160"
#
#
# class RealBuilder(AbstractBuilder):
# 	def addName(self):
# 		self.car.name = "Bentley"
#
# 	def addEngine(self):
# 		self.car.engine = "3-stroke"
#
# 	def addTyres(self):
# 		self.car.tyres = "MRF"
#
# 	def addSpeedometer(self):
# 		self.car.speedometer = "0-260"
#
#
# class Director():
# 	def __init__(self, builder):
# 		self._builder = builder
#
# 	def constructCar(self):
# 		self._builder.createNewCar()
# 		self._builder.addName()
# 		self._builder.addEngine()
# 		self._builder.addTyres()
# 		self._builder.addSpeedometer()
#
# 	def getCar(self):
# 		return self._builder.car
#
#
# concreteBuilder = ConcreteBuilder()
# director = Director(concreteBuilder)
#
# director.constructCar()
# carOne = director.getCar()
# print("Информация о первом авто:", carOne)
#
# realBuilder = RealBuilder()
# director = Director(realBuilder)
# director.constructCar()
# carTwo = director.getCar()
# print("Информация о втором авто:", carTwo)

### 2. Создайте приложение для приготовления пасты. Приложение должно уметь создавать минимум три вида пасты.
# Классы различной пасты должны иметь следующие методы:
# ■ Тип пасты;
# ■ Соус;
# ■ Начинка;
# ■ Добавки.
# Для реализации используйте порождающие паттерны.

# class Pasta():
# 	def __init__(self):
# 		self.name = None
# 		self.sauce = None
# 		self.filling = None
# 		self.additive = None
#
# 	def __str__(self):
# 		return '{} | {} | {} | {}'.format(self.name, self.sauce, self.filling, self.additive)
#
#
# class AbstractBuilder():
# 	def __init__(self):
# 		self.pasta = None
#
# 	def createNewCar(self):
# 		self.pasta = Pasta()
#
#
# class ConcreteBuilder(AbstractBuilder):
# 	def addName(self):
# 		self.pasta.name = "Спагетти"
#
# 	def addSauce(self):
# 		self.pasta.sauce = "карбонара"
#
# 	def addFilling(self):
# 		self.pasta.filling = "бекон"
#
# 	def addAdditive(self):
# 		self.pasta.additive = "чеснок"
#
#
# class RealBuilder(AbstractBuilder):
# 	def addName(self):
# 		self.pasta.name = "Лингуини"
#
# 	def addSauce(self):
# 		self.pasta.sauce = "болоньеза"
#
# 	def addFilling(self):
# 		self.pasta.filling = "фарш"
#
# 	def addAdditive(self):
# 		self.pasta.additive = "орегано"
#
#
# class DefiniteBuilder(AbstractBuilder):
# 	def addName(self):
# 		self.pasta.name = "Фузилли"
#
# 	def addSauce(self):
# 		self.pasta.sauce = "песто"
#
# 	def addFilling(self):
# 		self.pasta.filling = "орехи"
#
# 	def addAdditive(self):
# 		self.pasta.additive = "базилик"
#
# class Director():
# 	def __init__(self, builder):
# 		self._builder = builder
#
# 	def constructPasta(self):
# 		self._builder.createNewCar()
# 		self._builder.addName()
# 		self._builder.addSauce()
# 		self._builder.addFilling()
# 		self._builder.addAdditive()
#
# 	def getPasta(self):
# 		return self._builder.pasta
#
#
# concreteBuilder = ConcreteBuilder()
# director = Director(concreteBuilder)
#
# director.constructPasta()
# pastaOne = director.getPasta()
# print("Паста 1:", pastaOne)
#
# realBuilder = RealBuilder()
# director = Director(realBuilder)
# director.constructPasta()
# pastaTwo = director.getPasta()
# print("Паста 2:", pastaTwo)
#
# definiteBuilder = DefiniteBuilder()
# director = Director(definiteBuilder)
# director.constructPasta()
# pastaThree = director.getPasta()
# print("Паста 3:", pastaThree)


### 3. Создайте реализацию паттерна Prototype. Протестируйте работу созданного класса.
# import copy
# class Car:
#     def __init__(self):
#         self.name = "HONDA"
#         self.color = "Синий"
#         self.seats = "5"
#
#     def __str__(self):
#         return '{} | {} | {}'.format(self.name, self.color, self.seats)
#
# class Prototype:
#     def __init__(self):
#         self.clonedObjects = {}
#
#     def registerObject(self, name, obj):
#         self.clonedObjects[name] = obj
#
#     def delObject(self, name):
#         del self.clonedObjects[name]
#
#     def clone(self, name, **kwargs):
#         clonedObject = copy.deepcopy(self.clonedObjects.get(name))
#         clonedObject.__dict__.update(kwargs)
#         return clonedObject
#
# defaultCar = Car()
# prototype = Prototype()
# prototype.registerObject('авто', defaultCar)
#
# carOne = prototype.clone('авто')
# print("Информация о первом авто:", carOne)
#
# carTwo = prototype.clone('авто', color="Черный")
# print("Информация о втором авто:", carTwo)
######################################################################
# from abc import ABC, abstractmethod
#
#
# class Prototype(ABC):
#
#     @abstractmethod
#     def clone(self):
#         pass
#
#
# class Car(Prototype):
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#
#     def __operation__(self):
#         self.performed_operation = 'car'
#
#     def clone(self):
#         obj = Car(self.name, self.color)
#         obj.performed_operation = self.performed_operation
#         return obj

