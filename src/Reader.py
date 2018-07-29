import json
import csv
import urllib.request


def json_read(file):
    byte_content = file.read()
    json_content = byte_content.decode('utf8').replace("'", '"')
    objects = json.loads(json_content)
    return objects


def csv_read(file):
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    return reader


def read(file):

    objects = None
    if file.name.endswith('.json'):
        objects = json_read(file)
    elif file.name.endswith('.csv'):
        objects = csv_read(file)

    for obj in objects:
        name = obj['Name']
        company = obj['Company']
        email = obj['Email']
        phone = obj['Phone']
        interests = obj['Interests']
        yield {'name': name,
               'company': company,
               'email': email,
               'phone': phone,
               'interests': interests
               }


def make_number_as_russian(number):
    n = str(number).rsplit(' ', 1)[0]
    for ch in ['-', '(', ')', '.']:
        n = n.replace(ch, '')
    return "+" + n


def read_from_json_place_holder():
    url_to_json = "https://jsonplaceholder.typicode.com/users"
    with urllib.request.urlopen(url_to_json) as url:
        data = json.loads(url.read().decode())
        for obj in data:
            name = obj['name']
            company = obj['company']['name']
            email = obj['email']
            phone = make_number_as_russian(obj['phone'])
            interests = obj['company']['catchPhrase']
            yield {'name': name,
                   'company': company,
                   'email': email,
                   'phone': phone,
                   'interests': interests
                   }


