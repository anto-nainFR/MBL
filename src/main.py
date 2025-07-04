import sys

from utils.read_gpx import read_gpx
from utils.plot_gpx import plot_gpx

def print_coordinates(coordinates):
    """
    Prints the coordinates in a formatted way.
    
    :param coordinates: List of tuples containing latitude and longitude.
    """
    for lat, lon in coordinates:
        print(f"Latitude: {lat}, Longitude: {lon}")


def main(left_file:str, right_file:str):
    left_coordinates = read_gpx(left_file)
    right_coordinates = read_gpx(right_file)

    print("Left GPX Coordinates:")
    print_coordinates(left_coordinates)
    print("\nRight GPX Coordinates:")
    print_coordinates(right_coordinates)

    plot_gpx(left_coordinates, right_coordinates)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <left.gpx> <right.gpx>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])