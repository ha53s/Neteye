#!/usr/bin/env python3
# 45.33.32.156
#'DK8tKMOf9UMkLRfaVoXYHjgrUkDkJI9Z'
# premium key: pHHlgpFt8Ka3Stb5UlTxcaEwciOeF2QM

import subprocess
import folium
import webbrowser
import Display
import time
import shodan
import requests
import optparse
import re



def shodan_lookup():

    Ip = input("Enter ip to locate: ")

    try:
#Geolocation information for the IP
        info = api.host(Ip)
        Country = info.get('country_name')
        City = info.get('city')
        Lat = info.get('latitude')
        Long = info.get('longitude')
        Dom = info.get('domains', [])

        print(" ")
        print("\033[95m" + "   ~ Information About IP ~ " + "\033[0m")
        print("\033[95m" + "---------------------------------" + "\033[0m")
        print('IP Address:', Ip)
        time.sleep(1)
        print('Country:', Country)
        time.sleep(1)
        print('City:', City)
        time.sleep(1)
        print('Latitude:', Lat)
        time.sleep(1)
        print('Longitude:', Long)
        time.sleep(1)
        print('Domains:', Dom)
        time.sleep(1)
        print("\033[95m" + "Opening Map......" + "\033[0m")
        time.sleep(5)
#Create a folium map object
        C = [Lat, Long]
        Map = folium.Map(location=C, zoom_start=12)
        folium.Marker(location=C, popup=f'{City}, {Country}').add_to(Map)
        Map.save('IP_LOCATION.html')
# Open the map in the web browser
        webbrowser.open('IP_LOCATION.html')
    except shodan.APIError as e:
        print('Error:', e)


# Find the vendor of the specific MAC address.
def macLookup(): 

    macAdd = str(input("Enter the MAC address you want to look up: "))

    api_url = f"https://api.macvendors.com/{macAdd}"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:

            vendor = response.text
            print(f"Vendor: {vendor}")
        else:
            print("Failed to retrieve vendor information.")
    except requests.RequestException as e:
        print(f"Error: {e}")


# Scan the open port of specific IP address with the help of Nmap 
def portScan():

    target = input('Enter the target IP address to scan: ')
    port_range = input('Enter the Nmap port range (e.g., 1-1000): ')

    try:
        nmap_command = f'nmap -p {port_range} {target}'
        subprocess.run(nmap_command, shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print('Nmap Error:', e)



available_filters = {
    '1': 'country',
    '2': 'city',
    '3': 'port',
    '4': 'os',
    '5': 'hostname',
}
# A dictionary for filters and their regular expression format
filter_validators = {
        'country': lambda value: bool(re.match(r"^[\w\s]+$", value)),
        'city': lambda value: bool(re.match(r"^\w+$", value)),
        'port': lambda value: bool(re.match(r"^\d+$", value)),
        'os': lambda value: bool(re.match(r"^\w+$", value)),
        'hostname': lambda value: bool(re.match(r"^\w+$", value)),
    }
#Country : US, CN, saudi arabia
#Cities = ['NY', 'london']
#ports = 80
#operating_systems = ['windows', 'linux']
#host name = local, lan

#Fuction to chack the validity of the input
def get_user_input(message, validator=None):
        user_input = input(message)
        if validator is None or validator(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")
            return get_user_input(message, validator)

#Function to perform the search
def filteredSearch():
    filters = {}
    while True:
        print("\033[91m" + " Available filters: " + "\033[0m")
        print("\033[94m" + "1. Country" + "\033[0m")
        print("\033[94m" + "2. City" + "\033[0m")
        print("\033[94m" + "3. Port" + "\033[0m")
        print("\033[94m" + "4. OS" + "\033[0m")
        print("\033[94m" + "5. Hostname" + "\033[0m")
        # Getting the user input AND checking the format for the input
        filter_choice = get_user_input("Enter the number of the filter you want to apply (0 to perform the search): ", lambda input_val: input_val in available_filters or input_val == '0')
        if filter_choice == '0':
            break
        filter_choice = available_filters[filter_choice]
        filter_name = filter_choice
        filter_validator = filter_validators[filter_name]
        value = get_user_input(f"Enter the {filter_name} value: ", filter_validator)
        filters[filter_name] = value
        # Printing the chosed filters
        print("\033[91m" + " Current filters: " + "\033[0m")
        print(filters)

    try:
        # Combine the filters
        query = ""
        if filters:
            for i in filters:
                query += " " + i + " : \"" + filters[i] + "\""

            # Perform the search
            results = api.search(query)
        else:
            results = api.search('apache')

        print("\033[91m" + f"Total results found: {results['total']}" + "\033[0m")

        # Iterate over the results
        for result in results['matches']:
            print(f"IP: {result['ip_str']}")

    except shodan.APIError as e:
        print(f"Error: {e}")


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-k", '--key', dest="key", help="pHHlgpFt8Ka3Stb5UlTxcaEwciOeF2QM")
    (options, arguments) = parser.parse_args()
    return options



if __name__ == "__main__":
    Display.toolScreen()


options = get_arguments()
if not options.key:
    key = str(input("Enter you Shodan API key: "))
    if not key:
        print("No Key Supplied, Exiting the Program...")
else:
    key = options.key

api = shodan.Shodan(key)


def runFunction(option):
    if option == '1':
        shodan_lookup()


    elif option == '2':
       macLookup()


    elif option == '3':
        portScan()

    elif option == '4':
        filteredSearch()
        
    elif option == '5':
        print("Exiting the program...")
        time.sleep(2)
        quit()
    else:
        print("Invalid option.")


while True:
    Display.options()
    o = input("Enter your option >>> ")
    runFunction(o)

