
import requests



class ApiMethodsPageObject:

    def method_get(self, url):
        payload, headers = {}, {}
        response = requests.request("GET", url, headers=headers, data=payload)
        response_json = response.json()
        assert response.status_code == 200
        list = ["products", "id", "name", "price", "brand", "category"]
        for x in list:
            if x in response_json:
               response_success = True

        if response_success:
            return "List successful"






if __name__ == "__main__":
    get = ApiMethodsPageObject()
    print(get.method_get("https://automationexercise.com/api/productsList"))
