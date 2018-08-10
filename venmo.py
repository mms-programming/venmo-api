import requests
import json


def get_number_of_transactions(data):
    return len(data['data'])


def write_data_to_file(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    r = requests.get('https://venmo.com/api/v5/public?until=1533863818')
    json_response = r.json()
    print(json_response)
    print('The number of transactions was %d' % get_number_of_transactions(json_response))

    write_data_to_file(json_response, 'data3.json')