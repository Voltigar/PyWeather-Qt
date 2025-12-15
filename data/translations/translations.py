dict_fr = {
    # Thunderstorm
    "thunderstorm with light rain": "Orage avec pluie légère",
    "thunderstorm with rain": "Orage avec pluie",
    "thunderstorm with heavy rain": "Orage avec forte pluie",
    "light thunderstorm": "Orage léger",
    "thunderstorm": "Orage",
    "heavy thunderstorm": "Orage fort",
    "ragged thunderstorm": "Orage morcelé",
    "thunderstorm with light drizzle": "Orage avec bruine légère",
    "thunderstorm with drizzle": "Orage avec bruine",
    "thunderstorm with heavy drizzle": "Orage avec forte bruine",

    # Drizzle
    "light intensity drizzle": "Bruine légère",
    "drizzle": "Bruine",
    "heavy intensity drizzle": "Forte intensité de bruine",
    "light intensity drizzle rain": "Bruine légère avec pluie",
    "drizzle rain": "Bruine avec pluie",
    "heavy intensity drizzle rain": "Forte bruine avec pluie",
    "shower rain and drizzle": "Averse de pluie et bruine",
    "heavy shower rain and drizzle": "Forte averse de pluie et bruine",
    "shower drizzle": "Bruine de type averse",

    # Rain
    "light rain": "Pluie légère",
    "moderate rain": "Pluie modérée",
    "heavy intensity rain": "Pluie forte",
    "very heavy rain": "Pluie très forte",
    "extreme rain": "Pluie extrême",
    "freezing rain": "Pluie verglaçante",
    "light intensity shower rain": "Averse de pluie légère",
    "shower rain": "Averse",
    "heavy intensity shower rain": "Forte averse",
    "ragged shower rain": "Averse morcelée",

    # Snow
    "light snow": "Neige légère",
    "snow": "Neige",
    "heavy snow": "Forte neige",
    "sleet": "Neige fondue",
    "light shower sleet": "Averse légère de neige fondue",
    "shower sleet": "Averse de neige fondue",
    "light rain and snow": "Pluie légère et neige",
    "rain and snow": "Pluie et neige",
    "light shower snow": "Averse légère de neige",
    "shower snow": "Averse de neige",
    "heavy shower snow": "Forte averse de neige",

    # Atmosphere
    "mist": "Brume",
    "smoke": "Fumée",
    "haze": "Voile (haze)",
    "sand/dust whirls": "Tourbillons de sable/poussière",
    "fog": "Brouillard",
    "sand": "Sable",
    "dust": "Poussière",
    "volcanic ash": "Cendres volcaniques",
    "squalls": "Rafales",
    "tornado": "Tornade",

    # Clear & Clouds
    "clear sky": "Ciel dégagé",
    "few clouds": "Peu de nuages (11-25%)",
    "scattered clouds": "Nuages épars (25-50%)",
    "broken clouds": "Nuages fragmentés (51-84%)",
    "overcast clouds": "Ciel couvert (85-100%)"
}


dict_en = {
    # Thunderstorm
    "thunderstorm with light rain": "Thunderstorm with light rain",
    "thunderstorm with rain": "Thunderstorm with rain",
    "thunderstorm with heavy rain": "Thunderstorm with heavy rain",
    "light thunderstorm": "Light thunderstorm",
    "thunderstorm": "Thunderstorm",
    "heavy thunderstorm": "Heavy thunderstorm",
    "ragged thunderstorm": "Ragged thunderstorm",
    "thunderstorm with light drizzle": "Thunderstorm with light drizzle",
    "thunderstorm with drizzle": "Thunderstorm with drizzle",
    "thunderstorm with heavy drizzle": "Thunderstorm with heavy drizzle",
    
    # Drizzle
    "light intensity drizzle": "Light drizzle",
    "drizzle": "Drizzle",
    "heavy intensity drizzle": "Heavy drizzle",
    "light intensity drizzle rain": "Light drizzle rain",
    "drizzle rain": "Drizzle rain",
    "heavy intensity drizzle rain": "Heavy drizzle rain",
    "shower rain and drizzle": "Shower rain and drizzle",
    "heavy shower rain and drizzle": "Heavy shower rain and drizzle",
    "shower drizzle": "Shower drizzle",
    
    # Rain
    "light rain": "Light rain",
    "moderate rain": "Moderate rain",
    "heavy intensity rain": "Heavy rain",
    "very heavy rain": "Very heavy rain",
    "extreme rain": "Extreme rain",
    "freezing rain": "Freezing rain",
    "light intensity shower rain": "Light shower",
    "shower rain": "Shower",
    "heavy intensity shower rain": "Heavy shower",
    "ragged shower rain": "Ragged shower",
    
    # Snow
    "light snow": "Light snow",
    "snow": "Snow",
    "heavy snow": "Heavy snow",
    "sleet": "Sleet",
    "light shower sleet": "Light sleet shower",
    "shower sleet": "Sleet shower",
    "light rain and snow": "Light rain and snow",
    "rain and snow": "Rain and snow",
    "light shower snow": "Light snow shower",
    "shower snow": "Snow shower",
    "heavy shower snow": "Heavy snow shower",
    
    # Atmosphere
    "mist": "Mist",
    "smoke": "Smoke",
    "haze": "Haze",
    "sand/dust whirls": "Sand/dust whirls",
    "fog": "Fog",
    "sand": "Sand",
    "dust": "Dust",
    "volcanic ash": "Volcanic ash",
    "squalls": "Squalls",
    "tornado": "Tornado",
    
    # Clear & Clouds
    "clear sky": "Clear sky",
    "few clouds": "Few clouds (11-25%)",
    "scattered clouds": "Scattered clouds (25-50%)",
    "broken clouds": "Broken clouds (51-84%)",
    "overcast clouds": "Overcast clouds (85-100%)"
}

#-----------------------------------------------------------------------------------------------------------


ui_translations = {
    "fr": {
        "title": "Pyqt-Forecast",
        "placeholder": "Entrez le nom d'une ville",
        "button": "Obtenir la météo",
        "dark_mode": "Mode Sombre",
        "light_mode": "Mode Clair",
        "errors": {
            "bad_request": "Mauvaise Requête:\nvérifiez les informations saisies",
            "unauthorized": "Non Autorisé:\nclé API invalide",
            "forbidden": "Interdit:\nL'accès a été refusé",
            "not_found": "Introuvable:\nLa ville n'a pas été trouvée",
            "internal_error": "Erreur serveur:\nVeuillez réessayer plus tard",
            "bad_gateway": "Bad Gateway:\nRéponse invalide du serveur",
            "service_unavailable": "Service non disponible:\nLe serveur est hors-service",
            "gateway_timeout": "Gateway Timeout:\nPas de réponse du serveur",
            "http_error": "Erreur HTTP",
            "connection_error": "Erreur de connexion:\nVérifiez votre connexion internet",
            "timeout": "Timeout:\nLa requête a expiré",
            "too_many_redirects": "Too Many Redirects:\nVérifiez l'URL",
            "request_error": "Erreur de requête"
        }
    },
    "en": {
        "title": "Pyqt-Forecast",
        "placeholder": "Enter a city name",
        "button": "Get Weather",
        "dark_mode": "Dark Mode",
        "light_mode": "Light Mode",
        "errors": {
            "bad_request": "Bad Request:\ncheck the information entered",
            "unauthorized": "Unauthorized:\nAPI key is invalid",
            "forbidden": "Forbidden:\nAccess denied",
            "not_found": "Not Found:\nCity not found",
            "internal_error": "Internal Server Error:\nPlease try again later",
            "bad_gateway": "Bad Gateway:\nInvalid response from server",
            "service_unavailable": "Service Unavailable:\nServer is down",
            "gateway_timeout": "Gateway Timeout:\nNo response from server",
            "http_error": "HTTP Error",
            "connection_error": "Connection Error:\nCheck your internet connection",
            "timeout": "Timeout:\nRequest expired",
            "too_many_redirects": "Too Many Redirects:\nCheck the URL",
            "request_error": "Request Error"
        }
    }
}

#---------------------------------------------------------------------------------------------------------------

weather_emoji = {
    # Orages ⛈️
    200: "⛈️",  # Orage avec pluie légère
    201: "⛈️",  # Orage avec pluie
    202: "⛈️",  # Orage avec forte pluie
    210: "🌩️",  # Orage léger
    211: "🌩️",  # Orage
    212: "🌩️",  # Orage fort
    221: "🌩️",  # Orage morcelé
    230: "🌦️",  # Orage avec bruine légère
    231: "🌦️",  # Orage avec bruine
    232: "🌧️",  # Orage avec forte bruine

    # Bruine 🌦️
    300: "🌦️",  # Bruine légère
    301: "🌦️",  # Bruine
    302: "🌧️",  # Forte intensité de bruine
    310: "🌧️",  # Bruine légère avec pluie
    311: "🌧️",  # Bruine avec pluie
    312: "🌧️",  # Forte intensité de bruine avec pluie
    313: "🌧️",  # Pluie de bruine et bruine
    314: "🌧️",  # Forte pluie de bruine et bruine
    321: "🌧️",  # Bruine de type averse

    # Pluie 🌧️
    500: "🌦️",  # Pluie légère
    501: "🌧️",  # Pluie modérée
    502: "🌧️",  # Pluie forte
    503: "🌧️",  # Pluie très forte
    504: "🌧️",  # Pluie extrême
    511: "🌨️",  # Pluie verglaçante
    520: "🌦️",  # Averse de pluie légère
    521: "🌧️",  # Averse
    522: "🌧️",  # Forte averse
    531: "🌧️",  # Averse morcelée

    # Neige ❄️
    600: "🌨️",  # Neige légère
    601: "❄️",  # Neige
    602: "❄️",  # Forte neige
    611: "🌨️",  # Neige fondue
    612: "🌨️",  # Averse légère de neige fondue
    613: "🌨️",  # Averse de neige fondue
    615: "🌨️",  # Pluie légère et neige
    616: "🌨️",  # Pluie et neige
    620: "🌨️",  # Averse légère de neige
    621: "🌨️",  # Averse de neige
    622: "❄️",  # Forte averse de neige

    # Atmosphère 🌫️
    701: "🌫️",  # Brume
    711: "💨",  # Fumée
    721: "🌫️",  # Haze (voile)
    731: "🌪️",  # Tourbillon de sable/poussière
    741: "🌫️",  # Brouillard
    751: "🏜️",  # Sable
    761: "💨",  # Poussière
    762: "🌋",  # Cendres volcaniques
    771: "💨",  # Rafales
    781: "🌪️",  # Tornade

    # Ciel dégagé ☀️
    800: "☀️",  # Ciel dégagé

    # Nuages ☁️
    801: "🌤️",  # Peu de nuages (11-25%)
    802: "⛅",   # Nuages épars (25-50%)
    803: "🌥️",  # Nuages fragmentés (51-84%)
    804: "☁️"    # Couverture nuageuse complète (85-100%)
}
