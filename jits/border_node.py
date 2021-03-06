from node import Node
from car import Car
from car_queue import CarQueue


# Node that exists on the edge of the system. From this point cars enter/leave the environment.
# Connects to one intersection
class BorderNode(Node):
	def __init__(self, name, x, y):
		super().__init__(name, "border", x, y)
		self.connection = None
		self.q = CarQueue(-1)  # -1 for no maximum q-size

	def set_connection(self, neighbour):
		self.connection = neighbour

	def spawn_car(self, destination):
		self.q.add_car(Car(destination))

	def update_cars(self, time_step):
		car = self.q.get_car()
		if car is not None:
			directions = car.get_directions(time_step, self.x, self.y)
			if not self.connection.transfer_car(self, car):
				if not self.q.add_car_back(car):  # car is added back to queue
					print("CAR COULD NOT BE ADDED BACK TO QUEUE AT BORDER")

	def number_of_cars(self):
		return self.q.number_of_cars()

	@staticmethod
	def car_leaves_system(car):
		Car.removed_cars += 1
		return True

	def __str__(self):
		return "Border node: " + super().__str__() + " has {0} cars".format(self.number_of_cars())
