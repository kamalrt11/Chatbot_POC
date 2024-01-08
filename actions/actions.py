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


# weather Bot File

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet
# from rasa_sdk.executor import CollectingDispatcher
# import requests

# class ActionCheckWeather(Action):
    
#     def name(self)-> Text:
#         return "action_get_weather"
    
#     def run(self, dispatcher, tracker, domain):
#         api_key = '3305b446d97b67be5867f42e3cb15048'
#         loc = tracker.get_slot('location')
#         current= requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}'.format(loc, api_key)).json()
#         print(current)
        
#         country = current['sys']['country']
#         city = current['name']
#         condition = current['weather'][0]['main']
#         temperatue_c = current['main']['temp']
#         humidity = current['main']['humidity']
#         wind_mph = current['wind']['speed']
#         response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {}mph""".format(condition,city, temperatue_c,humidity, wind_mph)
        
#         dispatcher.utter_message(response)
#         return [SlotSet('location', loc)]




###################### Read Table Code

# import pandas as pd
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ReadExcelData(Action):
#     def name(self) -> Text:
#         return "action_read_excel_data"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         excel_file = 'MOCK_DATA.xlsx'  # Replace 'your_file.xlsx' with your file path
#         data = pd.read_excel(excel_file)

#         # Process the data here, for example, you can print it or use it in any way needed
#         # For demonstration purposes, let's just print the data
#         dispatcher.utter_message(text=f"Data from Excel: {data.to_string()}")

#         return []



###################### Product Details Code

# import pandas as pd
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class QueryProductDetails(Action):
#     def name(self) -> Text:
#         return "action_query_excel_data"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Assuming 'data/data.xlsx' is your file path
#         excel_file = 'MOCK_DATA.xlsx'

#         try:
#             data = pd.read_excel(excel_file)
#             product_id = tracker.get_slot("product_id")

#             if product_id:
#                 result = data[data['Product ID'] == int(product_id)]

#                 if not result.empty:
#                     output = result.to_string(index=False)
#                     dispatcher.utter_message(text=f"Details for Product ID {product_id}:\n{output}")
#                 else:
#                     dispatcher.utter_message(text=f"No details found for Product ID {product_id}")
#             else:
#                 dispatcher.utter_message(text="No Product ID found in slots.")
#         except Exception as e:
#             dispatcher.utter_message(text=f"Error: {str(e)}")

#         return []

###################### Architect Name From Software

# import pandas as pd
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class QueryProductDetails(Action):
#     def name(self) -> Text:
#         return "action_query_excel_data"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         excel_file = 'MOCK_DATA.xlsx'

#         try:
#             data = pd.read_excel(excel_file)
#             #software_name = tracker.latest_message.get('text')
#             software_name = tracker.get_slot("software_name")

#             if software_name:
#                 result = data[data['Software'] == software_name]

#                 if not result.empty:
#                     architect_name = result.iloc[0]['Architect']
#                     dispatcher.utter_message(text=f"Architect Name for {software_name} is {architect_name}")
#                 else:
#                     dispatcher.utter_message(text=f"No details found for {software_name}")
#             else:
#                 dispatcher.utter_message(text="No Software Name found in the input.")
#         except Exception as e:
#             dispatcher.utter_message(text=f"Error: {str(e)}")

#         return []


# import pandas as pd
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet

# class QueryProductDetails(Action):
#     def name(self) -> Text:
#         return "action_query_excel_data"

#     def __init__(self):
#         self.data = pd.read_excel('MOCK_DATA.xlsx')

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         try:
#             software_name = next(tracker.get_latest_entity_values("software_name"), None)
#             slot_name = "software_name"

#             if software_name:
#                 result = self.data[self.data['Software'].str.lower() == software_name.lower()]

#                 if not result.empty:
#                     architect_name = result.iloc[0]['Architect']
#                     dispatcher.utter_message(text=f"The architect for {software_name} is {architect_name}")
#                 else:
#                     dispatcher.utter_message(text=f"No architect details found for {software_name}")
#             else:
#                 dispatcher.utter_message(text="No software name found in the input.")

#             return [SlotSet(slot_name, software_name)]
#         except Exception as e:
#             dispatcher.utter_message(text=f"Error: {str(e)}")

#         return []

#Fetch Architect Name Using Software Name 

import pandas as pd
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


from fuzzywuzzy import fuzz
from fuzzywuzzy import process


class ActionAskForSoftware(Action):
    def name(self) -> Text:
        return "action_ask_for_software"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_ask_for_software")
        return []

#class ActionFetchArchitect(Action):
#    def name(self) -> Text:
#        return "action_fetch_architect"
#
#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#        software_name = tracker.get_slot('software')
#
#        # Load the Excel sheet into a pandas DataFrame
#        data = pd.read_excel('MOCK_DATA.xlsx')
#
#        # Search for the software and get the corresponding architect
#        row = data[data['Software'] == software_name]
#        if not row.empty:
#            architect = row['Architect'].values[0]
#            dispatcher.utter_message(text=f"The architect of {software_name} is {architect}")
#        else:
#            dispatcher.utter_message(response="utter_architect_not_found")
#
#        return [SlotSet("software", software_name)]



# class ActionFetchArchitect(Action):
#     def name(self) -> Text:
#         return "action_fetch_architect"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         software_name = tracker.get_slot('software')

#         # Load the Excel sheet into a pandas DataFrame
#         data = pd.read_excel('MOCK_DATA.xlsx')

#         # Fuzzy matching threshold (adjust as needed)
#         threshold = 40

#         # Search for the software using fuzzy matching
#         matched_software = None
#         highest_ratio = 0
#         for software in data['Software']:
#             ratio = fuzz.token_sort_ratio(software_name.lower(), str(software).lower())
#             if ratio > threshold and ratio > highest_ratio:
#                 highest_ratio = ratio
#                 matched_software = software

#         if matched_software:
#             # Get the corresponding architect for the matched software
#             row = data[data['Software'] == matched_software]
#             architect = row['Architect'].values[0]
#             date = row['Phaseout Date'].values[0]
#             dispatcher.utter_message(text=f"The architect of {matched_software} is {architect}")
#             dispatcher.utter_message(text=f"The Phaseout Date of {matched_software} is {date}")

#         else:
#             dispatcher.utter_message(response="utter_architect_not_found")

#         return [SlotSet("software", matched_software)]


class ActionFetchSoftwareInfo(Action):
    def name(self) -> Text:
        return "action_fetch_software_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # dispatcher.utter_message(text=f" Iam here")

        software_name = tracker.get_slot('software')
        # dispatcher.utter_message(text=f"{software_name}")

        data = pd.read_excel('MOCK_DATA.xlsx')

        user_events = [event for event in tracker.events if event.get("event") == "user"]

        prev_intent = None

        # if len(user_events) > 1:
        #     prev_intent = user_events[-2].get("parse_data", {}).get("intent", {}).get("name")
        # elif len(user_events) > 0:
        #     prev_intent = user_events[-1].get("parse_data", {}).get("intent", {}).get("name")

        if len(user_events) > 1:
            if user_events[-1].get("parse_data", {}).get("intent", {}).get("name") == "inform":
                prev_intent = user_events[-2].get("parse_data", {}).get("intent", {}).get("name")
            else:
                prev_intent = user_events[-1].get("parse_data", {}).get("intent", {}).get("name")

        matched_software = process.extractOne(software_name, data['Software'], scorer=fuzz.token_sort_ratio)

        if matched_software[1] >= 40:
            software_name = matched_software[0]

            row = data[data['Software'] == software_name]

            if not row.empty and prev_intent:
                if prev_intent == 'get_phaseout_date':
                    phaseout_date = row['Phaseout Date'].values[0]
                    dispatcher.utter_message(text=f"Phaseout Date of {software_name} is {phaseout_date}")
                    return [SlotSet("software", None)]

                elif prev_intent == 'get_vendor_name':
                    vendor_name = row['Vendor'].values[0]
                    dispatcher.utter_message(text=f"Vendor of {software_name} is {vendor_name}")
                    return [SlotSet("software", None)]

                elif prev_intent == 'check_license_required':
                    license_required = row['License Required'].values[0]
                    dispatcher.utter_message(text=f"License Status for {software_name}: {license_required}")
                    return [SlotSet("software", None)]

                elif prev_intent == 'check_tsc_status':
                    tsc_status = row['TSC Status'].values[0]
                    dispatcher.utter_message(text=f"TSC Status of {software_name}: {tsc_status}")
                    return [SlotSet("software", None)]

                elif prev_intent == 'get_installation_count':
                    installation_count = row['Install Count'].values[0]
                    dispatcher.utter_message(text=f"Installation Count of {software_name}: {installation_count}")
                    return [SlotSet("software", None)]

                elif prev_intent == 'get_architect':
                    architect = row['Architect'].values[0]
                    dispatcher.utter_message(text=f"The architect of {software_name} is {architect}")
                    return [SlotSet("software", None)]
            else:
                dispatcher.utter_message(response="utter_software_not_found")

            return [SlotSet("software", software_name)]
        else:
            dispatcher.utter_message(response="utter_software_not_found")
            return [SlotSet("software", None)]
