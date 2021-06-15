# import the library
import googlemaps
import json
import pprint
import time

API_KEY = 'AIzaSyB5aQxkMgu-c6wmPQ_s8RO_Ks_YEYjC3YA'
gmaps = googlemaps.Client(key = API_KEY)
placeids = []
radius = 5000
location = ['51.5399660615354', '-0.14398839643892516']

data = ['website', 'rating', 'user_ratings_total', 'name', 
 'international_phone_number', 'plus_code', 'formatted_address', 'place_id', 'business_status',
]
  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'amusement_park')
stored_results = []
i = 0
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('amusement_park.json', 'w') as f:
    json.dump(stored_results, f)

  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'art_gallery')
stored_results = []
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('art_gallery.json', 'w') as f:
    json.dump(stored_results, f)


  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'bakery')
stored_results = []
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)


with open('bakery.json', 'w') as f:
    json.dump(stored_results, f)

  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'bank')
stored_results = []
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('bank.json', 'w') as f:
    json.dump(stored_results, f)


  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'bar')
stored_results = []
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('bar.json', 'w') as f:
    json.dump(stored_results, f)

  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'beauty_salon')
stored_results = []
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('beauty_salon.json', 'w') as f:
    json.dump(stored_results, f)


  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'cafe')
stored_results = []
i = 0
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('cafe.json', 'w') as f:
    json.dump(stored_results, f)

  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'city_hall')
stored_results = []
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('city_hall.json', 'w') as f:
    json.dump(stored_results, f)


  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'clothing_store')
stored_results = []
i = 0
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)


with open('clothing_store.json', 'w') as f:
    json.dump(stored_results, f)

  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'dentist')
stored_results = []
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('dentist.json', 'w') as f:
    json.dump(stored_results, f)


  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'department_store')
stored_results = []
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('department_store.json', 'w') as f:
    json.dump(stored_results, f)

  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'drugstore')
stored_results = []
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('drugstore.json', 'w') as f:
    json.dump(stored_results, f)

  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'electronics_store')
stored_results = []
i = 0
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('electronics_store.json', 'w') as f:
    json.dump(stored_results, f)

  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'gym')
stored_results = []
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('gym.json', 'w') as f:
    json.dump(stored_results, f)


  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'hair_care')
stored_results = []
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('hair_care.json', 'w') as f:
    json.dump(stored_results, f)

  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'local_government_office')
stored_results = []
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('local_government_office.json', 'w') as f:
    json.dump(stored_results, f)


  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'meal_delivery')
stored_results = []
i = 0
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('meal_delivery.json', 'w') as f:
    json.dump(stored_results, f)

  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'meal_takeaway')
stored_results = []
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('meal_takeaway.json', 'w') as f:
    json.dump(stored_results, f)


  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'museum')
stored_results = []
i = 0
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('museum.json', 'w') as f:
    json.dump(stored_results, f)

  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'pet_store')
stored_results = []
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('pet_store.json', 'w') as f:
    json.dump(stored_results, f)

  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'pharmacy')
stored_results = []
i = 0
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('pharmacy.json', 'w') as f:
    json.dump(stored_results, f)

  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'physiotherapist')
stored_results = []
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('physiotherapist.json', 'w') as f:
    json.dump(stored_results, f)

  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'post_office')
stored_results = []
i = 0
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('post_office.json', 'w') as f:
    json.dump(stored_results, f)

  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'restaurant')
stored_results = []
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)
with open('restaurant.json', 'w') as f:
    json.dump(stored_results, f)


  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'spa')
stored_results = []
i = 0
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)

with open('spa.json', 'w') as f:
    json.dump(stored_results, f)

  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'store')
stored_results = []
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)
with open('store.json', 'w') as f:
    json.dump(stored_results, f)


  
places_result  = gmaps.places_nearby(location= location, radius = radius, open_now =False , type = 'supermarket')
stored_results = []
for place in places_result['results']:
    my_place_id = place['place_id']
    placeids.append(my_place_id)
    my_fields = data
    places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
    pprint.pprint(places_details['result'])
    stored_results.append(places_details['result'])
time.sleep(3)
try:
    luis  = gmaps.places_nearby(page_token = places_result['next_page_token'])
    for place in luis['results']:
        my_place_id = place['place_id']
        if my_place_id not in placeids:
            placeids.append(my_place_id)
            my_fields = data
            places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
            pprint.pprint(places_details['result'])
            stored_results.append(places_details['result'])
        else: 
            print('duplicated result')
    time.sleep(3)
    try:
        ze  = gmaps.places_nearby(page_token = luis['next_page_token'])
        for place in ze['results']:
            my_place_id = place['place_id']
            if my_place_id not in placeids:
                placeids.append(my_place_id)
                my_fields = data
                places_details  = gmaps.place(place_id= my_place_id , fields= my_fields)
                pprint.pprint(places_details['result'])
                stored_results.append(places_details['result'])
            else: 
                print('duplicated result')                
    except KeyError:
        print('erro aqui')
except KeyError:
    print('erro aqui')
print('primeiro passo')
time.sleep(3)
with open('supermarket.json', 'w') as f:
    json.dump(stored_results, f)



files=['amusement_park.json','art_gallery.json', 'bakery.json', 'bank.json','bar.json', 'beauty_salon.json', 
'cafe.json','city_hall.json', 'clothing_store.json', 'dentist.json','bar.json', 'department_store.json', 
'drugstore.json','electronics_store.json', 'gym.json', 'hair_care.json','local_government_office.json', 'meal_delivery.json', 
'meal_takeaway.json','museum.json', 'pet_store.json', 'pharmacy.json','physiotherapist.json', 'post_office.json', 
]

def merge_JsonFiles(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r') as infile:
            result.extend(json.load(infile))

    with open('CAMDEN.json', 'w') as output_file:
        json.dump(result, output_file)

merge_JsonFiles(files)