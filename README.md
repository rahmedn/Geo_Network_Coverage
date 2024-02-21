# Geo Network Coverage

## Overview

Geo Network Coverage Checker is a small API project that allows real estate agencies to check the network coverage (2G/3G/4G) for multiple addresses. The coverage is determined based on the presence of network towers within specific radii.

## Features

- **Address Lookup**: Given a list of addresses, the API retrieves network coverage information for each address.

- **Coverage Evaluation**: The coverage is evaluated for major network providers (Orange, SFR, Bouygues, Free) and for each technology (2G, 3G, 4G).

## Requirements

- Python 3.9
- FastAPI
- Pyproj
- Geopy
- requests
## Data Source
The CSV file (data/data.csv) contains network coverage measurements with columns for the operator, coordinates, and coverage for 2G, 3G, and 4G.

## Installation

1. Clone the repository

   ```bash
   git clone https://github.com/rahmedn/Geo_Network_Coverage.git
   cd Geo_Network_Coverage

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   
3. Run the FastAPI application
   ```bash
   uvicorn app:app --reload
4. Access the API at http://127.0.0.1:8000/docs in your browser

- POST /get_network_coverage/: Get network coverage for multiple addresses.
 - JSON Payload example

```json
   {
        
   "id1" : "157 boulevard Mac Donald 75019 Paris",
   "id4" : "5 avenue Anatole France 75007 Paris"
}
   
```
- Response Example:
```json
{
  "id1": {
    "Orange": {
      "2G": true,
      "3G": false,
      "4G": true
    },
    "SFR": {
      "2G": true,
      "3G": false,
      "4G": true
    },
    "Bouygues": {
      "2G": true,
      "3G": false,
      "4G": true
    },
    "Free": {
      "2G": true,
      "3G": false,
      "4G": true
    }
  },
  "id4": {
    "Orange": {
      "2G": true,
      "3G": false,
      "4G": true
    },
    "SFR": {
      "2G": true,
      "3G": false,
      "4G": true
    },
    "Bouygues": {
      "2G": true,
      "3G": false,
      "4G": true
    },
    "Free": {
      "2G": true,
      "3G": false,
      "4G": true
    }
  }
  }

```