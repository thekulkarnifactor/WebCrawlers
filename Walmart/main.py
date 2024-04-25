import configparser
import logging
import utils

def read_config():
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read('config.ini')

    # Access values from the configuration file
    debug_mode = config.getboolean('General', 'debug')
    log_level = config.get('General', 'log_level')
    db_name = config.get('Database', 'db_name')
    db_host = config.get('Database', 'db_host')
    db_port = config.get('Database', 'db_port')
    walmartSite = config.get('URL', 'walmartSite')
    searchItem = config.get('URL', 'searchItem')

    # Return a dictionary with the retrieved values
    config_values = {
        'debug_mode': debug_mode,
        'log_level': log_level,
        'db_name': db_name,
        'db_host': db_host,
        'db_port': db_port,
        'walmartSite' : walmartSite,
        'searchItem' : searchItem
    }

    return config_values

def app(config_data):
    if (config_data):
        print("INFO: Call to Utils")
        logging.info("INFO: Call to Utils")
        utils_obj = utils.HitSite
        utils_obj.hitsite_sel()

    else:
        print("ERROR: Data is not given")
        logging.ERROR("ERROR: Data is not given")

        
    
    
if __name__ == "__main__":
    config_data = read_config()
    utils(config_data)
    print("walmartSite:", config_data['walmartSite'])
    print("searchItem:", config_data['searchItem'])
