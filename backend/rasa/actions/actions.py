from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .utilities import fetch_car_info, fetch_car_listings, fetch_driver_info, fetch_image_url, fetch_team_info

class ActionListParticipants(Action):
    def name(self) -> Text:
        return "action_list_participants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        participant_type = tracker.get_slot("participant_type")

        if participant_type == "teams":
            participants_info = """
                <p>Every year around 100 teams drive the Nürburgring 24h.</p> \n
                <p>The most important teams in 2024 were:</p> \n
                <ul>
                    <li>Frikadelli Racing</li>
                    <li>Herbert Motorsport</li>
                    <li>Scherer Sport</li>
                    <li>Lionspeed GP</li>
                    <li>Red Bull ABT</li>
                    <li>Falken Motorsport</li>
                    <li>ROWE RACING</li>
                    <li>Manthey</li>
                    <li>Bilstein Motorsport</li>
                </ul> \n
                <p>Feel free to ask for more details on each of the teams above.</p>
            """

        elif participant_type == "cars":
            participants_info = """
                <p>In 2024 there were 127 cars taking part in the race.</p> \n
                <p>Here is a list of the most notable cars:</p> \n
                <ul>
                    <li>Ferrari 296 GT3</li>
                    <li>Mercedes AMG GT3</li>
                    <li>Porsche 911 GT3 R</li>
                    <li>Lamborghini Huracan GT3</li>
                    <li>Audi R8 GT3</li>
                    <li>Aston Martin Vantage GT3</li>
                    <li>BMW M4 GT3</li>
                    <li>Toyota Supra GT4</li>
                    <li>BMW M3 CSL</li>
                    <li>Dacia Logan</li>
                </ul> \n
                <p>Feel free to ask about more details on each of the cars above.</p>
            """

        elif participant_type == "drivers":
            participants_info = """
                <p>There are between three and four drivers per car and each driver 
                can drive in up to two cars. In 2024 there was a total of 493 drivers.</p> \n
                <p>Some of the top drivers are listed below:</p> \n
                <ul>
                    <li>Ricardo Feller</li>
                    <li>Frank Stippler</li>
                    <li>Kelvin van der Linde</li>
                    <li>Marco Mapelli</li>
                    <li>David Pittard</li>
                    <li>Dan Harper</li>
                    <li>Augusto Farfus</li>
                    <li>Maro Engel</li>
                    <li>Kevin Estre</li>
                </ul> \n
                <p>Feel free to ask about more details for each of the drivers above.</p>
            """ 
        else:
            participants_info = "Would you like to hear about teams, cars, or drivers?"  

        dispatcher.utter_message(text=participants_info)
        return []

class ActionProvideTeamDetail(Action):
    def name(self) -> Text:
        return "action_provide_team_detail"

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        team_name = tracker.get_slot("team_name")

        if team_name:
            team_info = fetch_team_info(team_name) 
            dispatcher.utter_message(text=team_info)
        return []


class ActionProvideCarDetail(Action):
    def name(self) -> Text:
        return "action_provide_car_detail"

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        car_name = tracker.get_slot("car_name")

        # Provide an image of the car here
        if car_name:
            car_image = fetch_image_url(car_name)
            if len(car_image) > 0:
                dispatcher.utter_message(image=car_image)

            # Return details about the car here
            car_info = fetch_car_info(car_name)
            dispatcher.utter_message(text=car_info)

            dispatcher.utter_message(
                text="Would you like so see available listings for this car?",
            )
               
            # Give the option to look for listings here
            dispatcher.utter_message(
                buttons=[
                    {"title": "Yes", "payload": "/show_listings"},
                    {"title": "No", "payload": "/deny_show_listings"},
                ]
            )

        # Fix
        return []


class ActionProvideDriverDetail(Action):
    def name(self) -> Text:
        return "action_provide_driver_detail"

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        driver_name = tracker.get_slot("driver_name")

        # Return an image of the driver
        driver_image = fetch_image_url(driver_name)
        if len(driver_image) > 0:
            dispatcher.utter_message(image=driver_image)    

        # Return detail infos about the driver
        if driver_name:
            driver_info = fetch_driver_info(driver_name)
            dispatcher.utter_message(text=driver_info)
        return []

class ActionShowListings(Action):
    def name(self) -> Text:
        return "action_show_listings"

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        car_name = tracker.get_slot("car_name")
        listing_data = fetch_car_listings(car_name)
        print(listing_data)

        # Only custom link format is used so there is no reason for tracking an additional type
        custom_message = {
            "name": listing_data.get("name"),
            "link": listing_data["result"]
        }

        # Fetch Data from Mobile.de API here
        dispatcher.utter_message(json_message=custom_message)

        return []

