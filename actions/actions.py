# This files contains your custom actions which can be used to run
# custom Python code.
#
# custom action

# import api requests functions
from api_requests import *

from typing import Any, Text, Dict, List
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ValidateCountryForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_country_form"

    @staticmethod
    def country_db() -> List[Text]:
        """Database of countries"""
        list_of_countries = get_countries()
        return list_of_countries

    def validate_country1(
        self,
        slot_value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate country value."""

        if slot_value.lower() in self.country_db():
            # validation succeeded, set the value of the "capital" slot to value
            # dispatcher.utter_message("this is capital")
            return {"country1": 'The capital is :'+get_capital(slot_value.lower())}
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            dispatcher.utter_message(f"please, Select another country that you want to check for")
            return {"country1": 'Not Found'}

    def validate_country2(
        self,
        slot_value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate country value."""

        if slot_value.lower() in self.country_db():
            # validation succeeded, set the value of the "population" slot to value
            # dispatcher.utter_message("this is population")
            return {"country2": 'The population is '+get_population(slot_value.lower())}
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            dispatcher.utter_message(f"please, Select another country that you want to check for")
            return {"country2": 'Not Found'}