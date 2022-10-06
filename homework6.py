#1. Создать класс TrafficLight (светофор).
#определить у него один атрибут color (цвет) и метод running (запуск);
#атрибут реализовать как приватный;
#в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
#проверить работу примера, создав экземпляр и вызвав описанный метод.
#адачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.

""" from time import sleep

class TrafficLight:
  __color = ['Красный', 'Желтый', 'Зеленый']

  def running(self):
    print('Горит ', self.__color[0])
    sleep(7)
    print('Горит ', self.__color[1])
    sleep(2)
    print('Горит ', self.__color[2])
    sleep(7)

traffic_light = TrafficLight()
traffic_light.running() """


#2. Реализовать класс Road (дорога).
#определить атрибуты: length (длина), width (ширина);
#значения атрибутов должны передаваться при создании экземпляра класса;
#атрибуты сделать защищёнными;
#определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
#использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
#проверить работу метода.
#Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
  def __init__(self, length, width):
    self._length = length
    self._width = width

  def calc(self):
    return f'Масса асфальта равна: {(self._length * self._width * 25 * 5)} кг'

road = Road(5000, 20)
print(road.calc())



#3. Реализовать базовый класс Worker (работник).
#определить атрибуты: name, surname, position (должность), income (доход);
#последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
#создать класс Position (должность) на базе класса Worker;
#в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
#проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
  def __init__(self, name, surname, position, income):
    self.name = name
    self.surname = surname
    self.position = position
    self._income = income

class Position(Worker):
  def get_full_name(self):
    return f'{self.name} {self.surname}'
  def get_full_profit(self):
    return f'{sum(self._income.values())}'

worker1 = Position('Ivan', 'Ivanov', 'Manager', {'profit': 20000, 'bonus': 20000})
print(worker1.get_full_name())
print(worker1.get_full_profit())


#4. Реализуйте базовый класс Car.
#у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
#опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
  def __init__(self, name, color, speed, is_police = False):
    self.name = name
    self.color = color
    self.speed = speed
    self.is_police = is_police
    print(f'Новая машина: {self.name} Цвет: {self.color} Полиция? {self.is_police}')

  def go(self):
    print(f'Машина {self.name} поехала')

  def stop(self):
    print(f'Машина {self.name} остановилась')  

  def turn(self, direction):
    print(f'Машина {self.name} повернула {"налево" if direction == 0 else "направо"}')

  def show_speed(self):
    print(f'Машина {self.name} едет со скоростью {self.speed}')

class TownCar(Car):
  def show_speed(self):
    print(f'Машина {self.name} едет со скоростью {self.speed} {"Превышение скорости!" if self.speed > 60 else "Скорость не превышена"}')

class WorkCar(Car):
  def show_speed(self):
    print(f'Машина {self.name} едет со скоростью {self.speed} {"Превышение скорости!" if self.speed > 40 else "Скорость не превышена"}')

class SportCar(Car):
  pass
class PoliceCar(Car):
  def __init__(self, name, color, speed, is_police = True):
    super().__init__(name, color, speed, is_police)

town_car = TownCar('Bus', 'yellow', 50)
town_car.go()
town_car.turn(0)
town_car.show_speed()

work_car = WorkCar('Truck', 'black', 70)
work_car.go()
work_car.turn(1)
work_car.show_speed()

police_car = PoliceCar('Police', 'black', 0)
police_car.stop()
police_car.show_speed()
print(police_car.is_police)


#5. Реализовать класс Stationery (канцелярская принадлежность).
#определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
#создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
#создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
  def __init__(self, title = 'Может рисовать'):
    self.title = title

  def draw(self):
    print('Запуск отрисовки')

class Pen(Stationery):
  def draw(self):
    print(f'Запуск отрисовки ручкой {self.title}')

class Pencil(Stationery):
  def draw(self):
    print(f'Запуск отрисовки карандашем {self.title}')

class Handler(Stationery):
  def draw(self):
    print(f'Запуск отрисовки маркером {self.title}')

st = Stationery()
st.draw()

pen = Pen('Parker')
pen.draw()

pencil = Pencil('Kon-I-Nor')
pencil.draw()

handler = Handler('Marker')
handler.draw()
