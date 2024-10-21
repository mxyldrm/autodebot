import requests
import time
from datetime import datetime
from common import logger, send_error_to_telegram, find_endpoint, get_vehicle_image_url, insert_car_to_database, delete_old_cars_from_database
from config import BASE_URL, RESPONSE_IDENTIFIER, BOT_NAME, HEADERS

# Function to check for new car listings and add them to the database
def check_new_listings():
    """
    Checks for new car listings on Auto.de and adds them to the database.
    """
    logger.info(f"{BOT_NAME} - Bot started working.")

    try:
        for page in range(1, 6):  # Process pages from 1 to 5
            url = BASE_URL.format(page)
            endpoints = find_endpoint(url, RESPONSE_IDENTIFIER, BOT_NAME)
            if not endpoints:
                logger.error(f"{BOT_NAME} - Endpoint not found for page {page}.")
                continue

            for endpoint in endpoints:
                process_listing_page(endpoint)

    except requests.RequestException as e:
        handle_request_error(e)

    except Exception as e:
        handle_generic_error(e)


def process_listing_page(endpoint):
    """
    Processes a specific page and adds car listings to the database.
    """
    response = requests.get(endpoint, headers=HEADERS)
    response.raise_for_status()

    data = response.json()
    car_listings = data.get('data', [])

    for car in car_listings:
        car_info = extract_car_info(car)
        if car_info:
            insert_car_to_database(car_info, BOT_NAME)


def extract_car_info(car):
    """
    Extracts necessary information from the car listing and returns it as a dict.
    """
    car_id = car.get('_id', None)
    if not car_id:
        return None

    make = car.get('mainData', {}).get('make', 'Unknown make')
    model = car.get('mainData', {}).get('model', 'Unknown model')
    sub_model = car.get('mainData', {}).get('subModel', 'Unknown sub-model')
    model_marka = f"{make} {model} {sub_model}"

    price = car.get('price', {}).get('currentSalesPrice', 'Unknown price')
    first_registration_year = car.get('mainData', {}).get('firstRegistrationYear', 'Unknown')
    link = f"https://www.auto.de/search/vehicle/{car_id}" if car_id else 'Link not available'
    main_image_id = car.get('metaData', {}).get('mainImageId', None)
    image_url = get_vehicle_image_url(car_id, main_image_id)

    transmission = get_transmission_type(car)
    gas_pump = get_fuel_type(car)
    speedometer = get_power_data(car)
    leaf = get_co2_emission(car)
    efficiency = get_combined_consumption(car)

    # Create car information
    return {
        'ID': car_id,
        'Model and Make': model_marka,
        'Price': price,
        'Link': link,
        'Image': image_url,
        'Company': 'autode',
        'Transmission': transmission,
        'Features': {
            'mileage_road': car.get('mainData', {}).get('mileage', 'Unknown'),
            'calendar': first_registration_year,
            'gas_pump': gas_pump,
            'speedometer': speedometer,
            'water_drop': efficiency,
            'leaf': leaf
        }
    }


def get_transmission_type(car):
    """
    Determines the transmission type from car data.
    """
    gearbox = car.get('driveSuspension', {}).get('gearbox', 'Unknown')
    return 'Manual' if gearbox == 'selector_gearbox_manualShift' else 'Automatic' if gearbox == 'selector_gearbox_automatic' else 'Unknown'


def get_fuel_type(car):
    """
    Determines the fuel type from car data.
    """
    fuel_type = car.get('consumption', {}).get('fuel', 'Unknown')
    return 'Petrol' if fuel_type == 'selector_fuel_petrol' else 'Diesel' if fuel_type == 'selector_fuel_diesel' else 'Hybrid'


def get_power_data(car):
    """
    Extracts power data (KW and PS) from car engine information.
    """
    engine_data = car.get('engineData', {})
    power_kw = engine_data.get('powerKW', 'Unknown')
    power_ps = engine_data.get('powerPS', 'Unknown')
    return f"{power_kw} KW ({power_ps} PS)"


def get_co2_emission(car):
    """
    Determines CO2 emissions from car data.
    """
    co2 = car.get('environmentEmissions', {}).get('co2', 'Unknown')
    return f"{co2} g" if co2 != 'Unknown' else co2


def get_combined_consumption(car):
    """
    Determines combined fuel consumption from car data.
    """
    return f"{car.get('consumption', {}).get('consumptionCombined', 'Unknown')} lt/100km"


def handle_request_error(e):
    """
    Function to be called in case of a request error.
    """
    error_message = f"{BOT_NAME} - An error occurred during the request: {e}"
    logger.error(error_message)
    send_error_to_telegram(error_message)


def handle_generic_error(e):
    """
    Function to be called in case of unexpected errors.
    """
    error_message = f"{BOT_NAME} - Unexpected error: {e}"
    logger.error(error_message)
    send_error_to_telegram(error_message)


# Main loop
def main():
    while True:
        try:
            logger.info(f"{BOT_NAME} - Main loop started.")
            check_new_listings()
            delete_old_cars_from_database()
        except Exception as e:
            handle_generic_error(e)

        time.sleep(60)  # Wait for 1 minute

if __name__ == "__main__":
    main()
