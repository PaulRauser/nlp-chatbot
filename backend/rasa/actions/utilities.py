from .wiki_api import fetch_wikipedia_summary
from .db import get_car_details, get_car_link, get_image, get_team_details

def check_team_name(name):
    team_names = [
        "Frikadelli Racing",
        "Herbert Motorsport",
        "Scherer Sport",
        "Lionspeed GP",
        "Red Bull Abt",
        "Falken Motorsport",
        "Walkenhorst Motorsport",
        "Rowe Racing",
        "Manthey Racing",
        "Bilstein Motorsport"
    ]

    name = name.strip().lower()

    best_match = None
    for entry in team_names:
        if name in entry.lower():
            if not best_match or len(entry) > len(best_match):
                best_match = entry

    print(f"Best team name match: {best_match}")
    return best_match

def check_car_name(name):
    car_names = [
        "Ferrari 296 GT3",
        "Mercedes AMG GT3",
        "Porsche 911 GT3",
        "Lamborghini Huracan GT3",
        "Audi R8 GT3",
        "Aston Martin Vantage GT3",
        "BMW M4 GT3",
        "Toyota Supra GT4",
        "BMW M3 CSL",
        "Dacia Logan"
    ]

    name = name.strip().lower()

    best_match = None
    for entry in car_names:
        if name in entry.lower():
            if not best_match or len(entry) > len(best_match):
                best_match = entry

    return best_match

def check_driver_name(name):
    driver_names = [
        "Ricardo Feller",
        "Frank Stippler",
        "Kelvin van der Linde",
        "Marco Mapelli",
        "David Pittard",
        "Dan Harper",
        "Augusto Farfus",
        "Maro Engel",
        "Kevin Estre"
    ]

    name = name.strip().lower()

    best_match = None
    for entry in driver_names:
        if name in entry.lower():
            if not best_match or len(entry) > len(best_match):
                best_match = entry

    return best_match

# Fetch image URL from DB - should handle wrong names accordingly
def fetch_image_url(name) -> str:
    car_match = check_car_name(name)
    driver_match = check_driver_name(name)

    best_match = None
    if car_match and driver_match:
        if len(car_match) > len(driver_match):
            best_match = car_match
        else:
            best_match = driver_match

    else:
        best_match = car_match if car_match else driver_match

    if best_match:
        return get_image(best_match)
    else:
        print(f"No matching name found for: {name}")
        return "I Can't find an image for this"

# Fetch data from Wikimedia
def fetch_driver_info(driver_name: str) -> str:
    checked_name = check_driver_name(driver_name)
    driver_info = fetch_wikipedia_summary(checked_name)
    return driver_info 

def fetch_team_info(team_name: str) -> str:
    checked_name = check_team_name(team_name)
    print(checked_name)
    team_details = None
    if checked_name:
        team_details = get_team_details(checked_name)
    if team_details:
        return team_details
    return "I can't find any info on this team. What else can I do for you?"

# Fetch car info from Database
def fetch_car_info(car_name: str) -> str:
    checked_name = check_car_name(car_name)
    car_details = None
    if(checked_name):
        car_details = get_car_details(checked_name)
    if car_details:
        return car_details

    return "I can't find any info about this car. Can I do something else for you?"

# Fetch listing from Mobile.de
def fetch_car_listings(car_name: str):
    checked_name = check_car_name(car_name)
    car_data = None
    if(checked_name):
        car_data = get_car_link(checked_name)
    if car_data:
        return car_data

    return "I can't find any listings for this. Is there something else I can do for you?"
