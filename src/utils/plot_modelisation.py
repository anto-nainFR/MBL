import matplotlib.pyplot as plt

def plot_modelisation(left_coordinates, right_coordinates, grid_points):
    """
    Plots the GPX routes and the grid points between them.
    
    :param left_coordinates: List of tuples (latitude, longitude) for the left GPX route.
    :param right_coordinates: List of tuples (latitude, longitude) for the right GPX route.
    :param grid_points: List of tuples (latitude, longitude) for the grid points.
    """
    left_lat, left_lon = zip(*left_coordinates)
    right_lat, right_lon = zip(*right_coordinates)
    grid_lat, grid_lon = zip(*grid_points)

    plt.figure(figsize=(10, 6))
    plt.plot(left_lon, left_lat, label='Left GPX', color='blue')
    plt.plot(right_lon, right_lat, label='Right GPX', color='red')
    plt.scatter(grid_lon, grid_lat, label='Modelisation Points', color='green', s=1)

    plt.title('GPX Road with Modelisation Points')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.show()