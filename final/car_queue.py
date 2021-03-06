from collections import deque

#Represents three lanes of the same incoming direction in an intersection
class CarQueue:
	def __init__(self, max_size):

		if max_size >= 0:
			self.q = list()
			self.maxlen = max_size
		else:
			self.q = list()
			self.maxlen = 9999999999

	def add_car(self, car):
		if self.maxlen is None or len(self.q) < self.maxlen:
			self.q.append(car)
			return True
		return False

	def add_car_back(self, car):
		if self.maxlen is None or len(self.q) < self.maxlen:
			self.q.append(car)
			return True
		return False

	def get_car(self):
		if len(self.q) == 0:
			return None
		car = self.q.pop()
		return car

	def get_car_for_direction(self, green_directions, car_position, x, y, neighborQueues):
		possible_directions = []
		if 0 in green_directions:
			possible_directions.append((car_position + 1) % 4)
		if 1 in green_directions:
			possible_directions.append((car_position + 2) % 4)
		if 2 in green_directions:
			possible_directions.append((car_position + 3) % 4)

		for index,car in enumerate(self.q):
			car_directions = car.get_directions( x, y)
			#if (possible_direction == car_direction and neighborQueues[car_direction].number_of_cars() < self.maxlen):
			if any(x in possible_directions for x in car_directions):
				returned_car = self.q.pop(index)
				return returned_car
			else:
				return None

	def number_of_cars(self):
		return len(self.q)

	def iterate_queue(self):
		total_waiting_time = 0
		for car in self.q:
			waiting_time = car.get_waiting_time()
			total_waiting_time += waiting_time
		return total_waiting_time

	def get_direction_amounts(self, time_step, x, y):
		directions = []
		direction_amounts = [0,0,0,0]
		for car in self.q:
			direction = car.get_directions(time_step, x, y)[0]
			directions.append(direction)

		# count each direction
		for direction in directions:
			if direction == 0:
				direction_amounts[0] += 1
			elif direction == 1:
				direction_amounts[1] += 1
			elif direction == 2:
				direction_amounts[2] += 1
			elif direction == 3:
				direction_amounts[3] += 1

		# Direction amounts is a list containing for n,e,s,w how many cars are waiting for that direction in the queue
		# Can be used to determine which light should be put on green
		print(direction_amounts)
		return direction_amounts




