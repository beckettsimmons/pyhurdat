import parse
import storm as Storm
from matplotlib import pyplot as plt

storms = parse.get_storms("../data/HURDAT.csv")

max_speeds = []
for storm in storms:
    max_speeds.append(Storm.maximum_wind_speed(storm))

max_speeds = sorted(max_speeds)
plt.plot(max_speeds)
