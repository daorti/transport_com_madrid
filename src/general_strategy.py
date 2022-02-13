from abc import abstractmethod, ABC
from geopy.distance import geodesic
import logging

logger = logging.getLogger()


class Transport(ABC):
    def __init__(self, dataframe, name, id, coordinates):
        """Abstract class who is going to receive the main params
            :param dataframe: dataset the object is going to work with
            :param name: str. Name of the searched station
            :param id: str/int. ID of the searched station
            :param coordinates: str. Latitude and longitude from the desirable point
        """
        self.dataframe = dataframe
        self.name = name
        self.id = id
        self.coordinates = coordinates

    @abstractmethod
    def display_info(self):
        pass

    @abstractmethod
    def find_station(self):
        pass

    def calculate_distances(self):
        """ Distance calculation from a given point to the selected station
            It calls the abstract method find_station to find the matched row of the dataframe
                :returns: integer with the distance between the two points, expressed in Kilometers
        """
        finder = self.find_station()
        station_loc = finder['COORDENADAS']
        logger.info('Calculating distance between point station and given coordinates')
        return round(geodesic(station_loc, self.coordinates).km, 2)

