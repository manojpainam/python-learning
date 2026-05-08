import json

def main():
    with open('minified.json', 'r') as file:
        json_data = json.load(file)

        # for element in json_data.get("data"):
        #     print("App Id : {}".format(element.get("appid")))
        #     print("App Name : {}".format(element.get("name")))
        #     print("Developer : {} \n".format(element.get("developer")))

        for element in json_data["data"]:
            print("#2App Id : {}".format(element.get("appid")))
            print("App Name : {}".format(element.get("name")))
            print("Developer : {} \n".format(element.get("developer")))


if __name__ == '__main__':
    main()