import matplotlib.pyplot as plt

def plot_gpx(left_coordinates: list, right_coordinates: list):
    """
    Plots two sets of GPX coordinates on a map.

    :param left_coordinates: List of tuples containing latitude and longitude for the left GPX file.
    :param right_coordinates: List of tuples containing latitude and longitude for the right GPX file.
    """
    left_lat, left_lon = zip(*left_coordinates)
    right_lat, right_lon = zip(*right_coordinates)

    plt.figure(figsize=(10, 6))
    plt.plot(left_lon, left_lat, label='Left GPX', color='blue', marker='.')
    plt.plot(right_lon, right_lat, label='Right GPX', color='red', marker='.')

    plt.title('GPX Coordinates')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.show()