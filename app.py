import json

with open('products.json','r') as file:
    products = json.load(file)

def main():
    # with open('minified.json', 'r') as file:
    #     json_data = json.load(file)

        # for element in json_data.get("data"):
        #     print("App Id : {}".format(element.get("appid")))
        #     print("App Name : {}".format(element.get("name")))
        #     print("Developer : {} \n".format(element.get("developer")))

        # for element in json_data["data"]:
        #     print("#2App Id : {}".format(element.get("appid")))
        #     print("App Name : {}".format(element.get("name")))
        #     print("Developer : {} \n".format(element.get("developer")))

    if products:
        for product in products:
            print("Name : {}".format(product.get("name")))

            for k,v in product.get("specifications").items():
                print("{} : {}".format(k, v))


            for review in product.get("reviews"):
                print("Review : {}".format(review))
            print("\n")


if __name__ == '__main__':
    main()