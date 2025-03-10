""" Contains the Google Routes API requests. """
import pandas as pd
import requests

from delivery_system.settings import GOOGLE_API_KEY

from delivery_system.models.cedi import CEDI


def get_waypoint(object) -> dict:
    """ Return the location of the object

    Parameters:
        object (Delivery or CEDI): The object to get the location.

    Returns:
        dict: The waypoint of the object.

    """
    return {
        "waypoint": {
            "location": {
                "latLng": {
                    "latitude": object.latitude,
                    "longitude": object.longitude
                }
            }
        }
    }


def get_nearest_cedi(delivery) -> tuple:
    """ Returns the nearest CEDI for the given location.

    Parameters:
        delivery (Delivery): Delivery Django model instance.

    Returns:
        tuple: A tuple containing the response data from Google Routes API.

    """
    cedis = CEDI.objects.order_by("id").all()
    print(cedis)
    if not cedis:
        return None

    data = {
        "origins": [get_waypoint(delivery)],
        "destinations": [get_waypoint(cedi) for cedi in cedis]
    }

    code, response = route_matrix_request(data)
    if code != 200:
        return None

    df = pd.DataFrame(response)

    min_distance_row = df.loc[df["distanceMeters"].idxmin()]

    return {
        "cedi": cedis[int(min_distance_row["destinationIndex"])],
        "distance": min_distance_row["distanceMeters"] / 1000,
        "duration": float(min_distance_row["duration"].rstrip("s")) / 60
    }


def route_matrix_request(data: dict) -> tuple:
    """ Sends a request to Google Routes API to compute the route matrix.

    Parameters:
        data (dict): The data to send in the request.

    Returns:
        tuple: A tuple containing the response data from Google Routes API.

    """
    response = requests.post(
        url="https://routes.googleapis.com/distanceMatrix/v2:computeRouteMatrix",
        json={
            "travelMode": "DRIVE",
            "routingPreference": "TRAFFIC_AWARE",
            **data
        },
        headers={
            "Content-Type": "application/json",
            "X-Goog-Api-Key": GOOGLE_API_KEY,
            "X-Goog-FieldMask": "originIndex,destinationIndex,duration,distanceMeters"
        }
    )

    return response.status_code, response.json()
