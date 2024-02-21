from utilities.api_helpers import get_coordinates
from fastapi import FastAPI, HTTPException
from utilities.utils import get_network_coverage_at_coordinates
from typing import Dict


app = FastAPI()


@app.post("/get_network_coverage/")
async def get_network_coverage(locations: Dict[str, str]):
    try:
        network_coverage_result = {}
        for key, value in locations.items():
            coordinates = get_coordinates(value)
            result = get_network_coverage_at_coordinates(coordinates)
            network_coverage_result[key] = result

        return network_coverage_result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

