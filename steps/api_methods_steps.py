from helper.page_objects.poo_api.api_methods_poo import ApiMethodsPageObject as apiMethods
from behave import given, when, then
import json


@given("API method")
def api_valitacion(context):
    with open("../settings/environment/datas_bo.json", "r") as file:
        data = json.load(file)
        for x in data:
            print(x)
    apiMethods.method_get(context.driver, "https://www.google.es")


