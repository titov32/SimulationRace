
from config import TRACKS, MOTOS, CARS

from race import Simulation


if __name__ == '__main__':
    simulation = Simulation(TRACKS, MOTOS, CARS)
    simulation.start()
    simulation.run()