# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# actions.py

import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSuggestSolution(Action):
    def name(self) -> Text:
        return "action_suggest_solution"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the detected health issue
        health_issue = tracker.latest_message['intent'].get('name')

        # Call the health API to get suggestions
        api_url = "https://medius-disease-prediction.p.rapidapi.com/api/v2/frequent-symptoms"
        params = {"status": "ok", "data": [health_issue]}

        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            suggestions = response.json().get("suggestions")
            response_text = f"Suggestions for {health_issue}: {', '.join(suggestions)}"
        else:
            response_text = "I'm sorry, I couldn't retrieve suggestions at the moment."

        # Send the suggestion to the user
        dispatcher.utter_message(text=response_text)

        return []
# import requests

# url = 

# querystring = {"period":"1m","birth_sex":"UNK","specialization":"general_practitioner","age":"27"}

# headers = {
# 	"X-RapidAPI-Key": "a8caf55ecdmshc987b761dc20c0fp18790bjsnd670983fef28",
# 	"X-RapidAPI-Host": "medius-disease-prediction.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())