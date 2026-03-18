from skyfield.api import load, EarthSatellite
from skyfield.timelib import Time
import datetime


def fetch_orbital_inventory():
    """
    IAN-SCP Data Acquisition Layer:
    Ingests TLE data for all active satellites.
    """
    # Loading real-time data from Celestrak (Active satellites)
    stations_url = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle'
    satellites = load.tle_file(stations_url)
    print(f"Successfully loaded {len(satellites)} active satellites into IAN-SCP.")[cite: 13]
    return satellites


def calculate_position(satellite, time_offset_hours=0):
    """
    Calculates the x, y, z position of a satellite.
    Supports the Risk Prediction Engine's modeling.
    """
    ts = load.timescale()
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=time_offset_hours)
    t = ts.from_datetime(now.replace(tzinfo=datetime.timezone.utc))

    geocentric = satellite.at(t)
    return geocentric.position.km


if __name__ == "__main__":
    inventory = fetch_orbital_inventory()
    # Example: Check position of the first satellite in the list
    sample_sat = inventory[0]
    pos = calculate_position(sample_sat)
    print(f"Tracking: {sample_sat.name} | Current Position (km): {pos}")