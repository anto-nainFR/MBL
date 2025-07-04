import numpy as np
from shapely.geometry import LineString, Polygon, Point

def create_grid(left_coordinates, right_coordinates, grid_density=50):
    """
    Create a grid of points between two GPX curves.
    
    :param left_coordinates: List of tuples (latitude, longitude) for the left curve
    :param right_coordinates: List of tuples (latitude, longitude) for the right curve
    :param grid_density: Density of the grid (number of points per axis)
    :return: List of tuples (latitude, longitude) of the grid points
    """
    # Convert lists in numpy arrays
    left_coords = np.array(left_coordinates)
    right_coords = np.array(right_coordinates)
    
    # Find the bounding box of the coordinates
    min_lat = min(left_coords[:, 0].min(), right_coords[:, 0].min())
    max_lat = max(left_coords[:, 0].max(), right_coords[:, 0].max())
    min_lon = min(left_coords[:, 1].min(), right_coords[:, 1].min())
    max_lon = max(left_coords[:, 1].max(), right_coords[:, 1].max())
    
    # Create the grid points
    lat_grid = np.linspace(min_lat, max_lat, grid_density)
    lon_grid = np.linspace(min_lon, max_lon, grid_density)
    
    grid_points = []
    
    # Create LineString objects for the left and right curves
    # Note: Shapely uses (longitude, latitude) for coordinates
    # while the input is in (latitude, longitude) format
    left_line = LineString([(lon, lat) for lat, lon in left_coordinates])
    right_line = LineString([(lon, lat) for lat, lon in right_coordinates])
    
    # Create a polygon by connecting the two curves
    # We reverse the order of one of the curves to close the polygon
    polygon_coords = list(left_line.coords) + list(reversed(right_line.coords))
    polygon = Polygon(polygon_coords)
    
    # Test each point in the grid to see if it is within the polygon
    for lat in lat_grid:
        for lon in lon_grid:
            point = Point(lon, lat)
            if polygon.contains(point):
                grid_points.append((lat, lon))
    
    return grid_points