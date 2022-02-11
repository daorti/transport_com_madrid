

from abc import ABC, abstractmethod
from geopy.distance import geodesic
import logging

# Logger
logger = logging.getLogger()


class TransportData(ABC):
    """Main, abstract class, that receives a file path by parameter. The goal of this
    class is to create subclasses that inherit from this main class, to obtain isolated
    data based on the kind of transport.
    """
    def __init__(self, data_path):
        """Constructor of TransportData class. Receives a file path by parameter.

        Params:
            - data_path: str expected, dataset path.
        """
        self.data_path = data_path

    @abstractmethod
    def get_transport_data(self):
        pass


class StationInfo(ABC):
    """Main, abstract class, that receives a Pandas DataFrame and a Station ID by
    parameter. The goal of this class is to create subclasses that inherit from this main
    class, to obtain information of a specific transport station, provided by the user.
    """
    def __init__(self, data, station_id):
        """Constructor of StationInfo class. Receives a Pandas DataFrame and a Station ID.
        The subclasses will return information of the requested station.
        Params:
            - data: Pandas DataFrame expected, transport data
            - station_id: int expected, Station ID which the user wants to get info.
        """
        self.data = data
        self.station_id = station_id

    @abstractmethod
    def get_full_info(self):
        pass


class GeodesicDistance:
    """Class to calculate the geodesic distance (in km) between two coordinates."""

    def __init__(self, coord1, coord2):
        """Class constructor. Receives two coordinates by parameter.

        Params:
            - coord1: list or tuple expected, first coordinate
            - coord1: list or tuple expected, first coordinate
        """
        self.coord1 = coord1
        self.coord2 = coord2

    @property
    def get_distance(self):
        """Returns the distance between two coordinates (in km)."""
        distance_km = geodesic(self.coord1, self.coord2).km
        return distance_km
