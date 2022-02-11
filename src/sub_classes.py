

import pandas as pd
from src.main_classes import TransportData, StationInfo
import logging

# Logger
logger = logging.getLogger()


class BiciMad(TransportData):
    """Subclass of TransportData. Create a specific BiciMad object, to return
    the specific BiciMad provided data (in Pandas DataFrame format).
    """

    def get_transport_data(self):
        """Returns a Pandas DataFrame object with BiciMAD data

        Returns:
            - data: Pandas DataFrame, BiciMAD specific data, provided by the client.
        """
        try:
            data = pd.read_csv(self.data_path) # Not Test path
            #data = pd.read_csv("/Users/antoniojimenez/Desktop/Transports_Madrid/ayto_madrid/data/bicimad_clean.csv") # Test path
            return data
        except Exception as e:
            logger.error('Error. Unable to obtain BiciMAD data.', e)
            return 'Error loading BiciMAD data.'


class Emt(TransportData):
    """Subclass of TransportData. Create a specific Emt object, to return
    the specific EMT provided data (in Pandas DataFrame format).
    """
    def get_transport_data(self):
        """Returns a Pandas DataFrame object with EMT data

        Returns:
            - data: Pandas DataFrame, EMT specific data, provided by the client.
        """
        try:
            data = pd.read_csv(self.data_path) # Not Test path
            #data = pd.read_csv("/Users/antoniojimenez/Desktop/Transports_Madrid/ayto_madrid/data/emt_clean.csv") # Test path
            return data
        except Exception as e:
            logger.error('Error. Unable to obtain EMT data.', e)
            return 'Error loading EMT data.'


class BiciMadStation(StationInfo):
    """Subclass of StationInfo. Create a specific BiciMadStation object,
    to get information from concrete BiciMAD stations.
    """
    def get_full_info(self):
        """Returns a dict with info of the station ID received by parameter.

        Params:
            -  station_id: int, unique ID of the BiciMAD station
        Returns:
            - station_info: dict, info of the required BiciMAD station
        """

        # Checking if 'station_id' type is int
        if not isinstance(self.station_id, int):
            logger.warning('Bad station ID received.')
            return "The station ID must be an integer."

        try:
            station_info = self.data[self.data.id == self.station_id].values[0]
        except IndexError:
            logger.warning('Bad station ID received.')
            return f"The station ID {self.station_id} doesn't exists."

        # Getting the required data from values
        try:
            total_bases = station_info[0]
            coordinate = (station_info[2], station_info[3])
            address = station_info[-1]

            info_dict = {'station_id': self.station_id,
                         'total_bases': total_bases,
                         'location': coordinate,
                         'address': address}
        except IndexError:
            logger.critical('Unexpected error accessing to the data.')
            return 'An unexpected error occurred. The program will close.'

        logger.info('Data successfully obtained.')
        return info_dict


class EmtStation(StationInfo):
    """Subclass of StationInfo. Create a specific EmtStation object,
    to get information from concrete EMT stations.
    """

    def get_full_info(self):
        """Returns a dict with info of the station ID received by parameter.

            Params:
                -  station_id: int, unique ID of the BiciMAD station
            Returns:
                - station_info: dict, info of the required BiciMAD station
        """

        # Checking if 'station_id' type is int
        if not isinstance(self.station_id, int):
            logger.warning('Bad station ID received.')
            return "The station ID must be an integer."

        try:
            station_info = self.data[self.data.id == self.station_id].values[0]
        except IndexError:
            logger.warning('Bad station ID received.')
            return f"The station ID {self.station_id} doesn't exists."

        # Getting the required data from values
        try:
            address = station_info[1]
            district = station_info[2]
            coordinate = (station_info[3], station_info[-1])

            info_dict = {'station_id': self.station_id,
                         'address': address,
                         'district': district,
                         'location': coordinate}
        except IndexError:
            logger.critical('Unexpected error accessing to the data.')
            return 'An unexpected error occurred. The program will close.'

        logger.info('Data successfully obtained.')
        return info_dict
