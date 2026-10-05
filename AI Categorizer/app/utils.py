from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="ai_categorizer")


def reverse_geocode(latitude: float, longitude: float):
    """
    Convert latitude and longitude into a readable address.
    """

    try:
        location = geolocator.reverse(
            (latitude, longitude),
            language="en",
        )

        if not location:
            return None

        address = location.raw.get("address", {})

        return {
            "latitude": latitude,
            "longitude": longitude,
            "place_name": location.address.split(",")[0],
            "address": location.address,
            "city": address.get("city")
            or address.get("town")
            or address.get("village"),
            "district": address.get("state_district"),
            "state": address.get("state"),
            "country": address.get("country"),
            "postal_code": address.get("postcode"),
            "google_maps_url": (
                f"https://maps.google.com/?q={latitude},{longitude}"
            ),
        }

    except Exception:
        return None