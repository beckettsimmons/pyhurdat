import parser
import storm as Storm

storms = parser.get_storms("../data/HURDAT.csv")

max_speeds = []
for storm in storms:
    max_speeds.append(Storm.maximum_wind_speed(storm))
