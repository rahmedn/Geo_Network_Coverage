import requests
from typing import List
from fastapi import HTTPException


def get_coordinates(address: str) -> List[float]:
    """
    Get geographic coordinates (longitude, latitude) for a given address using the adresse.data.gouv.fr API.

    Parameters:
    - address (str): The address for which coordinates are to be retrieved.

    Returns:
    - List[float]: A list containing the geographic coordinates [longitude, latitude].

    Raises:
    - HTTPException: Raised with a 404 status code if the address is not found.
    """
    api_url = "https://api-adresse.data.gouv.fr/search/"
    response = requests.get(api_url, params={"q": address, "limit": 1})
    data = response.json()

    if data["features"]:
        coordinates = data["features"][0]["geometry"]["coordinates"]
        return coordinates
    else:
        raise HTTPException(status_code=404, detail="Address not found")