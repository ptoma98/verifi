# Verifi Interview

## Script to get current weather
To run this script, please install the prerequisites, then follow the directions below.

### Prerequisites

If you don't have Python 3 installed, do the following:

For MacOS:

1. Install XCode CLI Tools:
`xcode-select --install`

2. Install Brew:
`ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

3. Brew Install Python 3:
`brew install python3`

For Other Platforms:
1. Download and run one of the platform installers provided on python.org:

    Windows: https://www.python.org/downloads/windows/
    Linux/Unix: https://www.python.org/downloads/source/

Next, clone the repository from GitHub:
`git clone https://github.com/ptoma98/verifi.git && cd verifi`

Finally, install the dependencies:
`pip3 install -r requirements.txt`

### Running the script:
To run the script you need an Open Weather API key. This should have been provided to
you by email. If not you can also create one by following these steps:

https://openweathermap.org/appid

The script by default outputs the weather in L.A:
```
$ python3 get_weather.py --key <YOUR_OPEN_WEATHER_API_KEY>
Current Los Angeles Weather: clear sky, current temperature is 89.19 degrees fahrenheit, low of 75, with a high of 102. 
```

To get the weather in other cities call the script with the --city argument:
```
$ python3 get_weather.py --city "Buenos Aires" --key <YOUR_OPEN_WEATHER_API_KEY>
Current Buenos Aires Weather: clear sky, current temperature is 52.29 degrees fahrenheit, low of 51.01, with a high of 54.
```
