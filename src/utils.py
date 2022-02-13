import pandas as pd
import yaml
from src.bicimad_strategy import BICIMAD
from src.emt_strategy import EMT
import logging
from geopy.distance import geodesic

with open('../config/config.yml', 'r') as stream:
    config = yaml.safe_load(stream)

logger = logging.getLogger()


def checking_config_params():
    """Checks the main config params: name, ID, transport type
        Returns:
                - Error if the transport  type is not BICIMAD or EMT
                - Error if the name is not a string
                - If the ID is not a string, change the type to str and returns correct
                - Correct in the rest of cases
    """
    logger.debug('Checking params')
    if type(config['transport_type']) != str or config['transport_type'].upper() not in ['BICIMAD', 'EMT']:
        return 'Error: Transport type is not correct'
    if type(config['name']) != str:
        return 'Error: Introduce a correct name in str format'
    if type(config['id']) != str:
        config['id'] = str(config['id'])
        return 'Correct'
    else:
        return 'Correct'


def check_empty_dataset(dataset):
    """Checks if the given object is a dataframe and if it´s empty
        :param dataset: DataFrame
        :returns:
            - String 'Not a dataframe' if the object is not that type
            - String 'The search has results' if is not an empty dataframe
        :raises:
            - TypeError exception if the dataset is empty
    """
    if type(dataset) != pd.core.frame.DataFrame:
        return 'Not a dataframe'
    elif dataset.empty:
        logger.warning('The search has no results')
        raise TypeError('Empty dataframe')
    else:
        return 'The search has results'



def checking_coordinates_params():
    """Checks the coordinates params
    :return:
        - String 'Correct' if the geodesic function works and gives a distance under 70 km, as a threshold
        - In any other case: String 'Introduce correct coordinates of Madrid'
    """
    logger.debug('Checking coordinates')
    try:
        geodesic('-3.6956047, 40.4440297', config['coordinates']) < 70
        return 'Correct'
    except:
        return 'Introduce correct coordinates of Madrid'


def charging_dataset():
    """Charging the dataset the program is going to work with
    :returns
        - BICIMAD dataframe charged if config param "transport_type" is BICIMAD
        - EMT dataframe charged  if config param "transport_type" is EMT
        - String 'Transport type defined is no available' in any othe case
    """
    if config['transport_type'].upper() == 'BICIMAD':
        bicimad = pd.read_csv('../data/bicimad_df_cleaned.csv', sep=',', dtype=str)
        logger.info('BICIMAD dataset charged')
        return bicimad

    elif config['transport_type'].upper() == 'EMT':
        emt = pd.read_csv('../data/emt_df_cleaned.csv', sep=',')
        logger.info('EMT dataset charged')
        return emt

    else:
        return 'Transport type defined is no available'


def creating_transport_object():
    """
    It creates the object that inherits from abstract Transport class.
    The class takes the arguments from the Transport class and from the charging_datset function
        :return:
            - The object instantiated if transport_type param is BICIMAD or EMT
            - In any other case, it logs a warning
    """

    if config['transport_type'].upper() == 'BICIMAD':
        logger.info('Creating BICIMAD object')
        return BICIMAD(charging_dataset(), config['name'], config['id'], config['coordinates'])

    elif config['transport_type'].upper() == 'EMT':
        logger.info('Creating EMT object')
        return EMT(charging_dataset(), config['name'], config['id'], config['coordinates'])

    else:
        return logger.warning('Transport type defined is no available')

