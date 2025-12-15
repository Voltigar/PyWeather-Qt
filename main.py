#Python Weather App using the PyQt lib and the OpenWeatherMap API

import sys
import requests
import json
import os
from pathlib import Path
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QComboBox, QInputDialog, QMessageBox)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from data.translations.translations import dict_fr, dict_en, weather_emoji, ui_translations

CONFIG_PATH = Path.home() / ".pyweatherqt_app_config.json" #Path where the json file that contain the api key will be stored

def load_api_key(): #This will load the api_key if the config path exists
    if CONFIG_PATH.exists():
        try:
            return json.loads(CONFIG_PATH.read_text()).get("api_key")
        except Exception:
            return None
    return None

def save_api_key(key): #This will save the api key into a json file
    CONFIG_PATH.write_text(json.dumps({"api_key": key}))
    

class WeatherApp(QWidget): #Main class of the program
    def __init__(self):    #The constructor, to initialize the window and the pyqt elements
        super().__init__()
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
        self.setFixedSize(800, 700)
        self.current_language = "fr"
        self.temperature_unit = "°C"
        self.city_label = QLabel("PyWeather Qt", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Obtenir la météo",self) #keep in mind that the text is mainly in french, but can be changed for english
        self.temperature_label = QLabel(self) #placeholder : 15°C // This is for the temperature text
        self.emoji_label = QLabel(self) #placeholder : ☀️ // this is for the emoji to illustrate the weather
        self.description_label = QLabel(self) #placeholder : ensoleillé // this is for the description of the weather
        self.change_language_button = QComboBox(self)
        self.change_unit = QComboBox(self)
        self.set_api = QPushButton("API key", self)
        
        self.api_key = load_api_key()
        if not self.api_key: #This will be first prompted to the user to enter an API key since there is not one
            QMessageBox.information(self, "No API Key", "There is not an API key, please click the 'API_key' button to enter one")
        
        self.setFocus()
        self.initUI()
        
    
    def initUI(self): #This will initialize the UI with the layout and widgets
        self.setWindowTitle("PyWeather QT")
        
        base_dir = os.path.dirname(os.path.abspath(__file__)) #To setup correctly the icon path
        icon_path = os.path.join(base_dir, "ui", "ressources", "PyWeather QT logo.svg") 
        self.setWindowIcon(QIcon(icon_path))  
        
        # Horizontal Layout, mainly for the language button and dark mode button
        hbox = QHBoxLayout()
        hbox.addWidget(self.change_language_button, alignment=Qt.AlignmentFlag.AlignLeft)
        hbox.addWidget(self.change_unit, alignment=Qt.AlignmentFlag.AlignRight)
        
        # Vertical Layout, this is the main layout for the rest of the UI elements
        vbox = QVBoxLayout()
        
        vbox.addLayout(hbox)
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input, alignment=Qt.AlignmentFlag.AlignCenter) #For the search bar
        vbox.addWidget(self.get_weather_button, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        vbox.addWidget(self.set_api, alignment= Qt.AlignmentFlag.AlignLeft)
        
        self.setLayout(vbox)
        
        self.city_input.setFixedSize(600, 70)
        self.get_weather_button.setFixedSize(500, 70)
    
        
        # Alignements
        self.city_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.city_input.setAlignment(Qt.AlignmentFlag.AlignCenter) #For the placeholder text on the search bar
        self.temperature_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        
        # Placeholders text
        self.city_input.setPlaceholderText("Entrez le nom d'une ville")
        self.change_language_button.setPlaceholderText("Langue")
        self.change_language_button.addItem("Français")
        self.change_language_button.addItem("English")
        self.change_unit.addItem("Celsius")
        self.change_unit.addItem("Fahrenheit")
        
        
        # Object names
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.change_language_button.setObjectName("language_button")
        self.change_unit.setObjectName("change_unit")
        self.set_api.setObjectName("set_api")
        
        
        
        # Style Sheets
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: creato-display;
                padding: 10px;
            }
            QLabel#city_label{
                font-size: 60px; 
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                background-color: hsl(18, 96%, 53%);
            }
            QPushButton#get_weather_button:hover{
                background-color: hsl(18, 96%, 63%);
            }
            QPushButton#get_weather_button:pressed{
                background-color: hsl(18, 96%, 43%);
            }
            QLabel#temperature_label{
                font-size: 60px;
            }
            QLabel#emoji_label{
                font-size: 90px;
                font-family: segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 35px;
            }
            QComboBox#language_button{
                font-family: creato-display;
                font-size: 14px;
                padding: 5px 15px;
                max-height: 40px;
                max-width: 150px;
            }
            QComboBox#change_unit{
                font-family: creato-display;
                font-size: 14px;
                padding: 5px 15px;
                max-height: 40px;
                max-width: 150px;
            }
            QPushButton#set_api{
                font-family: creato-display;
                font-size: 14px;
                padding: 5px 15px;
                max-height: 40px;
                max-width: 150px;
            }
        """)
        
        #Connecting buttons to their respective functions
        self.get_weather_button.clicked.connect(self.get_weather)
        self.change_language_button.currentIndexChanged.connect(self.change_language)
        self.change_unit.currentIndexChanged.connect(self.toggle_unit)
        self.set_api.clicked.connect(self.on_set_key)
        

    def get_weather(self): #Function that call the openweathermap api
        api_key = self.api_key
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data["cod"] == 200:
                self.display_weather(data)
        
        except requests.exceptions.HTTPError as http_error: #for handling error and understand them better
            match response.status_code:
                case 400:
                    self.display_error(ui_translations[self.current_language]["errors"]["bad_request"])
                case 401:
                    self.display_error(ui_translations[self.current_language]["errors"]["unauthorized"])
                case 403:
                    self.display_error(ui_translations[self.current_language]["errors"]["forbidden"])
                case 404:
                    self.display_error(ui_translations[self.current_language]["errors"]["not_found"])
                case 500:
                    self.display_error(ui_translations[self.current_language]["errors"]["internal_error"])
                case 502:
                    self.display_error(ui_translations[self.current_language]["errors"]["bad_gateway"])
                case 503:
                    self.display_error(ui_translations[self.current_language]["errors"]["service_unavailable"])
                case 504:
                    self.display_error(ui_translations[self.current_language]["errors"]["gateway_timeout"])
                case _:
                    self.display_error(f"{ui_translations[self.current_language]['errors']['http_error']}:\n{http_error}")
                    
            
        except requests.exceptions.ConnectionError:
            self.display_error(ui_translations[self.current_language]["errors"]["connection_error"])
        except requests.exceptions.Timeout:
            self.display_error(ui_translations[self.current_language]["errors"]["timeout"])
        except requests.exceptions.TooManyRedirects:
            self.display_error(ui_translations[self.current_language]["errors"]["too_many_redirects"])
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"{ui_translations[self.current_language]['errors']['request_error']}:\n{req_error}")
            
    
    def display_error(self, message): #For displaying the error on the app itself
        self.temperature_label.setStyleSheet("font-size: 30px")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()
    
    def display_weather(self, data): #For displaying the weather with the temp, description of the weather and the emoji
        self.temperature_label.setStyleSheet("font-size: 60px;")
        self.current_temp_k = data["main"]["temp"]
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        
        weather_dict = dict_fr if self.current_language == "fr" else dict_en
        
        if self.temperature_unit == "°C": #This convert the kelvin unit that openweathermap api's use by default, to celsius and fahrenheit units
            temp = self.current_temp_k - 273.15
            unit = "°C"
        else:
            temp = (self.current_temp_k - 273.15) * 9/5 + 32
            unit = "°F"
        
        self.temperature_label.setText(f"{temp:.0f}{unit}")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_dict[weather_description])
    
    @staticmethod    
    def get_weather_emoji(weather_id): #For displaying the correct emoji
        return weather_emoji.get(weather_id, "❓")
    
    def change_language(self, index): #For changing the language to french or english using the language button
        if index == 0:
            self.current_language = "fr"
        elif index == 1:
            self.current_language = "en"
        self.update_ui_texts()
        
    def update_ui_texts(self): #To update the language of the app
        lang = ui_translations[self.current_language]
        
        self.city_input.setPlaceholderText(lang["placeholder"])
        self.get_weather_button.setText(lang["button"])

        
    def toggle_unit(self, index): #To change the unit from celsius to fahrenheit using the temperature unit button
        if index == 0:
            self.temperature_unit = "°C"
        elif index == 1:
            self.temperature_unit = "°F"
        if self.temperature_label.text() and "°" in self.temperature_label.text():
            self.refresh_temperature_display()
        
    def refresh_temperature_display(self): #To update the temperature unit of the app
        if self.current_temp_k:
            if self.temperature_unit == "°C":
                temp = self.current_temp_k - 273.15
                unit = "°C"
            else:
                temp = (self.current_temp_k - 273.15) * 9/5 + 32
                unit = "°F"
            self.temperature_label.setText(f"{temp:.0f}{unit}")
            
                
    def on_set_key(self): #An input dialog to prompt the user to enter the api key after they pressed the 'api key' button, this will be saved to a .json file
        text, ok = QInputDialog.getText(self, "Enter API Key", "Please enter your API key:") 
        if ok and text:
            save_api_key(text.strip())
            self.api_key = text.strip()
            QMessageBox.information(self, "Saved", "API key saved successfully.") #a message box will appear to tell the user that their api key has been saved
         
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec())

