

import utils
import logging.config


def main():

    # 1. Settings ..............................................................

    # 1.1. Logger
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger()

    # 1.2. Variables from YML config file
    logger.info('Reading YAML file.')
    config_dict = utils.read_config_file()

    logger.info('Obtaining data from YAML file.')
    transportation_type = config_dict['transportation_type']
    station_id = config_dict['station_id']
    coordinate_1 = tuple(map(float, config_dict['coordinate_1'].split(', ')))
    coordinate_2 = tuple(map(float, config_dict['coordinate_2'].split(', ')))

    # 2. Functional testing ....................................................

    logger.info('Starting functional testing...')
    print('STARTING FUNCTIONAL TESTING...')

    # 2.1. Station info
    print('\n- Getting station info...')
    station_info = utils.get_station_info(transportation=transportation_type,
                                          station_id=station_id)

    print('Station Info:', station_info)


    # 2.2. Distance between two coordinates
    print('\n- Getting distance...')
    distance = utils.get_distance(point_a=coordinate_1,
                                  point_b=coordinate_2)

    print(distance)
    logger.info('Functional testing done. No problems found.')


if __name__ == "__main__":
    main()




