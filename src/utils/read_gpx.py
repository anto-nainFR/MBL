import gpxpy

def read_gpx(file_path:str) -> list:
    """
    Reads a GPX file and returns a list of tuples containing latitude and longitude.

    :param file_path: Path to the GPX file.
    :return: List of tuples with (latitude, longitude).
    """
    with open(file_path, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    coordinates = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                coordinates.append((point.latitude, point.longitude))

    return coordinates