import yaml
import requests

url = "http://localhost:2224/rand_character"
def main():
    #make an API call to /rand_character
    resp = requests.get(url)

    #get the JSON from the response
    data = resp.json()

    #convert the data to YAML
    text = yaml.dump(data)
    text = f"{data['name']} is affiliated with {stringifyList(data['affiliations'])}\nand appears in {stringifyList(data['books'])}."

    print(text)

def stringifyList(data):
    result = ""
    for x in range(0, len(data)):
        result = result + data[x]
        if x != len(data) - 1:
            if x == len(data) - 2 and len(data) > 2:
                result = result + ', and '
            elif len(data) == 2:
                result = result + ' and '
            else:
                result = result + ', '
    return result

if __name__ == '__main__':
    main()