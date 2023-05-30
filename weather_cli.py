import requests
import json
import argparse
from tqdm import tqdm
from termcolor import colored
from pyfiglet import Figlet
from tabulate import tabulate

# Fetch weather data from the OpenWeatherMap API
def fetch_weather_data(API_KEY, city):
    """
    Fetches weather data from the OpenWeatherMap API.

    Args:
        API_KEY (str): API key for accessing the OpenWeatherMap API.
        city (str): Name of the city for which to fetch weather data.

    Returns:
        dict: Weather data in JSON format.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

# Parse the weather data and extract relevant information
def parse_weather_data(data):
    """
    Parses the weather data and extracts relevant information.

    Args:
        data (dict): Weather data in JSON format.

    Returns:
        dict: Parsed weather data containing description, temperature, humidity, and wind speed.
    """
    if data['cod'] == '404':
        raise ValueError(f"City Not Found: ")

    parsed_data = {
        "Description": data["weather"][0]["description"].capitalize(),
        "Temperature": f"{data['main']['temp']} K",
        "Humidity": f"{data['main']['humidity']} %",
        "Wind Speed": f"{data['wind']['speed']} m/s"
    }
    return parsed_data

# Display ASCII art for the weather tool
def display_ascii_art():
    """
    Displays ASCII art for the weather tool.
    """
    f = Figlet(font="digital")
    ascii_art = f.renderText("Weather")
    colored_ascii_art = colored(ascii_art, "cyan")
    print(colored_ascii_art)

# Display the weather data in a tabular format
def display_weather_data(parsed_data):
    """
    Displays the weather data in a tabular format.

    Args:
        parsed_data (dict): Parsed weather data.
    """
    headers = [colored(header, attrs=['bold']) for header in parsed_data.keys()]
    colored_data = [headers, list(parsed_data.values())]
    print()
    print(colored("Weather Information", "green", attrs=["bold"]))
    print(tabulate(colored_data, tablefmt="fancy_grid"))
    print()

# Main function to execute the weather tool
def main():
    parser = argparse.ArgumentParser(description="Weather Command-Line Tool")
    parser.add_argument("city", metavar="CITY", type=str, help="Name of the city")
    args = parser.parse_args()

    city = args.city
    API_KEY = '4bdddf331c84b6da7e0f6be53a55a65c'

    try:
        display_ascii_art()

        # Progress bar for fetching weather data
        with tqdm(desc="Fetching weather data", unit="B", unit_scale=True) as progress_bar:
            data = fetch_weather_data(API_KEY, city)
            progress_bar.update(1)

        if data["cod"] == "404":
            print(colored("Error: City not found.", "red", attrs=["bold"]))
        else:
            parsed_data = parse_weather_data(data)
            display_weather_data(parsed_data)
    except requests.exceptions.RequestException as e:
        print(colored(f"Error: Failed to retrieve weather data. {str(e)}", "red", attrs=["bold"]))

if __name__ == "__main__":
    main()
