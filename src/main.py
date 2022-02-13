import logging.config
from src.utils import *

logging.config.fileConfig('../config/logger.conf')
logger = logging.getLogger()

with open('../config/config.yml', 'r') as stream:
    config = yaml.safe_load(stream)
logger.info('Variables from YML file charged')

if __name__ == "__main__":

    if checking_config_params() == 'Correct':
        try:
            transport = creating_transport_object()
        except:
            logger.critical('Error creating the object')
        try:
            check_empty_dataset(transport.display_info())
            # TITLE
            print(f'SEARCHING INFO OF {config["transport_type"]} SELECTED STATION \n')

            # GENERAL INFO OF THE STATION
            print(f'General info of {config["name"]}:')
            print(transport.find_station(), '\n')
            logger.info('Station general info displayed')

            # SPECIFIC INFO OF THE STATION
            print(f'Specific info of {config["name"]}:')
            print(transport.display_info(), '\n')
            logger.info('Station specific info displayed')

            # DISTANCE BETWEEN TWO POINTS
            print(f'Distance from {config["name"]} to the selected coordinates is:')
            if checking_coordinates_params() == 'Correct':
                print(f'{transport.calculate_distances()} km')
            else:
                logger.warning('Incorrect coordinates. Introduce correct coordinates of Madrid')
        except:
            logger.critical('ID and name not found in the dataset')

    else:
        logger.critical(checking_config_params())

logger.info('Program finished')

