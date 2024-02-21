import pyproj
from data.loader import load_data


def lamber93_to_gps(x, y):

    lambert = pyproj.Transformer.from_crs('EPSG:2154', 'EPSG:4326', always_xy=True)
    longitude, latitude = lambert.transform(x, y)

    return longitude, latitude


def calculate_distance(position1, position2):
    """
    Calculate the distance between two positions.

    Parameters:
    - position1 (tuple): Tuple containing X and Y coordinates of the first position.
    - position2 (tuple): Tuple containing X and Y coordinates of the second position.

    Returns:
    - float: Euclidean distance between the two positions.
    """

    x1, y1 = position1
    x2, y2 = position2
    x_diff = x1 - x2
    y_diff = y1 - y2
    return (x_diff ** 2 + y_diff ** 2) ** 0.5


def get_radius_for_technology(technology: str) -> float:
    """
    Get the radius for a specific technology.

    Parameters:
    - technology (str): The technology type ("2G", "3G", or "4G").

    Returns:
    - float: The radius for the specified technology.
    """
    if technology == "2G":
        return 30
    elif technology == "3G":
        return 5
    elif technology == "4G":
        return 10
    else:
        raise ValueError("Unsupported technology: {}".format(technology))


def is_position_covered(position1, position2, radius):
    """
    Check if a position is covered within a specific radius.

    Parameters:
    - position1 (tuple): Tuple containing X and Y coordinates of the first position.
    - position2 (tuple): Tuple containing X and Y coordinates of the second position.
    - radius (float): The coverage radius.

    Returns:
    - bool: True if the position is covered, False otherwise.
    """
    distance = calculate_distance(position1, position2)
    return distance <= radius


def get_network_coverage_at_coordinates(coordinates):
    """
    Retrieves network coverage information for a given set of coordinates.

    Parameters:
    - coordinates (tuple): A tuple containing latitude and longitude coordinates.

    Returns:
    - dict: A dictionary containing network coverage information for different providers.

    """
    network_coverage = {}
    data = load_data('data/data.csv')

    for row in data:
        provider = row["Operateur"]

        if provider not in network_coverage:
            network_coverage[provider] = {}

            # Convert Lambert 93 coordinates to GPS coordinates
            x_lambert = float(row["x"])
            y_lambert = float(row["y"])
            longitude, latitude = lamber93_to_gps(x_lambert, y_lambert)

            # Check network coverage based on distance
            coverage = {
                "2G": is_position_covered(coordinates, (longitude, latitude), get_radius_for_technology("2G")),
                "3G": is_position_covered(coordinates, (longitude, latitude), get_radius_for_technology("3G")),
                "4G": is_position_covered(coordinates, (longitude, latitude), get_radius_for_technology("4G"))
            }

            network_coverage[provider] = coverage

    return network_coverage
