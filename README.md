# Project: Weather Forecast Command-Line Tool


### Introduction:
The Weather Forecast Command-Line Tool is a Python-based application that allows users to retrieve the current weather forecast for a specific city. The tool leverages the OpenWeatherMap API to fetch weather data and utilises Python for data parsing and error handling. This project aims to demonstrate how GitHub Copilot can assist developers in implementing API usage, data parsing, and error handling efficiently.

### Functionality:
Accept City Name: The command-line tool accepts the name of a city as a command-line argument. This allows users to specify the city for which they want to retrieve the weather forecast.
Fetch Weather Data: The tool utilises the OpenWeatherMap API to fetch weather data for the specified city. It constructs the API URL by combining the base URL, API key, and the provided city name. Then, it sends an HTTP GET request to the API endpoint using the requests library and retrieves the response containing the weather information.
Data Parsing: Once the weather data is fetched, the tool parses the JSON response to extract relevant information. The parse_weather_data function is responsible for parsing the data and extracting the weather description, temperature, humidity, and wind speed. This function utilises JSON parsing techniques to navigate through the data structure and retrieve the required fields.
Display Weather Information: After parsing the weather data, the tool presents the extracted information to the user in a tabular format. The display_weather_data function utilises the tabulate library to format the data into a visually appealing table. The weather information, including the description, temperature, humidity, and wind speed, is displayed in separate columns for easy readability.
Error Handling: The tool incorporates error handling mechanisms to handle potential errors that may occur during the execution. If the specified city is not found, the fetch_weather_data function raises a ValueError and displays an appropriate error message to the user, indicating that the city was not found. This ensures that the tool gracefully handles scenarios where the requested city does not exist in the weather data.

### GitHub Copilot Integration:
GitHub Copilot, an AI-powered code completion tool, has been utilised to enhance the development process of the Weather Forecast Command-Line Tool. It has played a significant role in improving various aspects of the project:
API Usage: Copilot provides suggestions for constructing the API URL, including the base URL and API key, and assists in sending HTTP requests using the requests library. It offers code completions for performing GET requests and handling API responses efficiently.
Data Parsing: Copilot suggests code snippets for parsing JSON data and extracting specific fields. It assists in navigating through the complex JSON structure, allowing for easy access to the desired weather information. Copilot's suggestions enhance the data parsing process, making it more accurate and concise.
Error Handling: Copilot identifies potential error scenarios, such as the city not being found in the weather data, and suggests error handling mechanisms. It provides insights into handling exceptions and raising appropriate error messages to ensure a robust error-handling approach.
General Code Completions: Throughout the development process, Copilot offers code completions for variable names, function names, and imports. It helps improve code quality by suggesting meaningful names and relevant imports,reducing the chances of syntax errors and enhancing overall readability.
By leveraging Copilot's AI capabilities, developers can streamline the implementation of API usage, data parsing, and error handling, resulting in more efficient and reliable code.

### Dependencies:
The Weather Forecast Command-Line Tool relies on the following external libraries:
requests: The requests library is used to make HTTP requests to fetch weather data from the OpenWeatherMap API. It simplifies the process of sending GET requests and handling API responses.
tqdm: The tqdm library is employed to display progress bars during the fetching of weather data. It provides visual feedback to the user, indicating the progress of the data retrieval process.
termcolor: The termcolor library enables the printing of coloured text in the console. It enhances the visual presentation of the ASCII art and error messages, making them more noticeable and user-friendly.
pyfiglet: The pyfiglet library is utilised for generating ASCII art. It allows the display of stylized text, enhancing the visual appeal of the tool's name in the console.
tabulate: The tabulate library is used for formatting tabular data. It helps present the weather information in a structured and visually appealing manner, facilitating better readability.

### Conclusion:
The Weather Forecast Command-Line Tool demonstrates how GitHub Copilot can significantly assist developers in implementing API usage, data parsing, and error handling. By providing accurate code completions and suggestions, Copilot enhances productivity and reduces the development time required for these tasks. The tool showcases the potential of AI-powered code completion tools in streamlining the development process and ensuring efficient utilisation of external APIs. Through its integration with Copilot, the Weather Forecast Command-Line Tool exemplifies the benefits of leveraging AI capabilities to simplify complex programming tasks and improve code quality.


### Working:
### Code :
![image](https://github.com/utkarsh-chaurasia/Weather-Forecasting-Tool/assets/52343042/19f77d9a-7658-4e24-9546-437115cae7df)



### Terminal Code Execution : 
### On entering correct City
![image](https://github.com/utkarsh-chaurasia/Weather-Forecasting-Tool/assets/52343042/4703c401-102e-4534-9999-171c6d93298c)



### On entering incorrect city
![image](https://github.com/utkarsh-chaurasia/Weather-Forecasting-Tool/assets/52343042/812b8c0e-3784-41b3-b149-e02003d06fe9)


 

