import sys
from random import choice, randint
from map import Map
from car import Car
from paths import path_dict, border_names
from tqdm import tqdm
import numpy as np
from new_global_traffic_light_combinations import combinations
import matplotlib.pyplot as plt

def main(argv):

	max_q_size = 50
	traffic_map = Map(max_q_size)

	n_time_steps = 10000
	iterations = 10
	leaving_cars = [0] * (n_time_steps)
	for i in tqdm(range(iterations)):
		traffic_map.reset()
		Car.reset_number_of_cars(Car)

		for t in range(0, n_time_steps):

			# time_step(traffic_map)

			# if t % 10 == 0:  # update traffic lights once every 10 time steps
			# 	traffic_map.update_traffic_lights(combinations[np.random.randint(traffic_map.action_size)])
			# traffic_map.update_cars(t)

			action = np.random.randint(traffic_map.action_size)

			new_state, reward, done, _ = traffic_map.step(action, t)

			leaving_cars[t] += (Car.get_number_of_cars(Car)[1]/iterations)

		traffic_map.display_map()

		n_cars = Car.get_number_of_cars(Car)
		print("")
		print("{0} cars were added to the system, {1} cars have left the system".format(n_cars[0], n_cars[1]))
		print("{0} cars are still in system".format(traffic_map.number_of_cars()))
		print("{0} cars have disappeared".format(n_cars[0] - n_cars[1] - traffic_map.number_of_cars()))
		print("random dirs: " + str(Car.random_direction))

	plt.plot(leaving_cars)
	plt.ylabel('#cars that have left the system')
	plt.xlabel('Step')
	plt.show()


def time_step(traffic_map):
	n_cars = 1
	for c in range(n_cars):
		start = choice(border_names)
		end = choice(border_names)
		while start == end:
			end = choice(border_names)
		traffic_map.spawn_car(start, end)


if __name__ == "__main__":
	main(sys.argv)
