from src.general_strategy import Transport
import logging

logger = logging.getLogger("")


class EMT(Transport):
    def find_station(self):
        """Checks in the charging datasets the id or name match
            :Return: The matched row of the dataframe
        """
        return self.dataframe[(self.dataframe['IDESTACION'].isin([self.id])) |
                              (self.dataframe['DENOMINACION'].isin([self.name]))]

    def display_info(self):
        """Calls to find_station function to find the matched row of the dataframe
            Returns: Only two columns of the row, the name of the station and the lines
        """
        finder = self.find_station()
        return finder[['DENOMINACION', 'LINEAS']]


