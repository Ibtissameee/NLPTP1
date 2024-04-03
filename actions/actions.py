# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
restaurant_dict = {
        'italian': ['Pepe Nero', 'La Palle A Pizza'],
        'asian': ['Nigiri House', 'Tokyo Sushi'],
        'moroccan': ['Al Kasbah Restaurant', 'Tajine City'],
        'fast food': ['Beau Burger', 'Snack Sa7bi']
    }
    
class ActionSuggestRestaurant(Action):

     def name(self) -> Text:
         return "action_suggest_restaurants"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         cuisine_type = tracker.get_slot("cuisine_type")
         if cuisine_type:
             restaurants_name = find_restaurant(cuisine_type.lower())
             if restaurants_name:
                 restaurants = ", ".join(restaurants_name) 
                 dispatcher.utter_message(template="utter_suggest_restaurants", restaurants_name=restaurants, cuisine_type=cuisine_type)
             else:
                 dispatcher.utter_message("I'm sorry, I couldn't find any restaurants for that cuisine.")
         else:
                dispatcher.utter_message("I'm sorry, I didn't understand your cuisine preference.")
         print("Cuisine Type:", cuisine_type)
         return []
def find_restaurant(cuisine):
    
    return restaurant_dict.get(cuisine)