from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionListParticipants(Action):
    def name(self) -> Text:
        return "action_list_participants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        participant_type = tracker.get_slot("participant_type")

        if participant_type == "teams":
            participants_info = """
                Every year around 100 teams drive the Nürburgring 24h.\n
                The most important teams in 2024 were:
                - Frikadelli Racing
                - Herbert Motorsport
                - Scherer Sport
                - Lionspeed GP
                - Red Bull ABT
                - Falken Motorsport
                - ROWE RACING
                - Manthey
                - Bilstein Motorsport\n
                Feel free to ask for details on each of these teams.
            """

        elif participant_type == "cars":
            participants_info = """
                In 2024 there were 127 cars taking part in the race. \n
                Here is a list of the most notable cars: \n
                - Ferrari 296 GT3
                - Mercedes-AMG GT3
                - Porsche 911 GT3 R
                - Lamborghini Huracan GT3
                - Audi R8 GT3 
                - Aston Martin Vantage GT3
                - BMW M4 GT3
                - Toyota GR Supra GT4
                - BMW M3 CSL
                - Dacia Logan\n
                Feel free to ask about details on each of these cars.
            """

        elif participant_type == "drivers":
            participants_info = """
                There are between three and four drivers per car and each driver can drive in 
                up to two cars. In 2024 there was a total of 493 drivers.\n
                Some of the top drivers are listed below:
                - Vincent Kolb
                - Ricardo Feller
                - Frank Stippler
                - Kelvin Van der Linde
                - Marco Mapelli
                - David Pittard
                - Daniel Harper
                - Augusto Farfus
                - Maro Engel
                - Kevin Estre\n
                Feel free to ask about details for each of these drivers.
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
        # Fetch and provide specific details about the team
        team_info = f"{team_name} is known for..."
        dispatcher.utter_message(text=team_info)
        return []


class ActionProvideCarDetail(Action):
    def name(self) -> Text:
        return "action_provide_car_detail"

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        car_name = tracker.get_slot("car_name")
        # Fetch and provide specific details about the car
        car_info = f"The {car_name} is a high-performance vehicle..."
        dispatcher.utter_message(text=car_info)
        return []


class ActionProvideDriverDetail(Action):
    def name(self) -> Text:
        return "action_provide_driver_detail"

    def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        driver_name = tracker.get_slot("driver_name")
        # Fetch and provide specific details about the driver
        driver_info = f"{driver_name} is a skilled driver..."
        dispatcher.utter_message(text=driver_info)
        return []
