
import requests
from bs4 import BeautifulSoup

def get_flight_departures(airport_code):
    url = f'https://flightaware.com/live/airport/{airport_code}/departures'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    flights_table = soup.find('table', {'id': 'departuresTable'})
    flights = flights_table.find_all('tr')[1:]  # Skip the header row

    departures = []
    for flight in flights:
        columns = flight.find_all('td')
        departures.append({
            'airline': columns[0].text.strip(),
            'flight_number': columns[1].text.strip(),
            'destination': columns[2].text.strip(),
            'departure_time': columns[3].text.strip(),
            'status': columns[4].text.strip()
        })

    return departures

airport_code = input('Enter the airport code: ')
departures = get_flight_departures(airport_code)

print(f"Departures from {airport_code}:")
for departure in departures:
    print(f"{departure['airline']} {departure['flight_number']} to {departure['destination']} at {departure['departure_time']} ({departure['status']})")

