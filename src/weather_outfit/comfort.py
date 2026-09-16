

def build_environment_profile(apparent_temperature,wind_speed,precipitation):
    profile = {
        "warmth_need" : 0.0,
        "rain_protection_need" : 0.0,
        "wind_protection_need" : 0.0,
        "breathability_need" : 0.0
    }
    
    if apparent_temperature <= 40:
        profile["warmth_need"] = 1.0
    elif apparent_temperature <= 50:
        profile["warmth_need"] = 0.8
    elif apparent_temperature <= 60:
        profile["warmth_need"] = 0.6
    elif apparent_temperature <= 70:
        profile["warmth_need"] = 0.4
    elif apparent_temperature <= 80:
        profile["warmth_need"] = 0.2


    if precipitation >= 0.30:
        profile["rain_protection_need"] = 1.0
    elif precipitation >= 0.10:
        profile["rain_protection_need"] = 0.7
    elif precipitation > 0:
        profile["rain_protection_need"] = 0.4


    if wind_speed >= 25:
        profile["wind_protection_need"] = 1.0
    elif wind_speed >= 15:
        profile["wind_protection_need"] = 0.7
    elif wind_speed >= 8:
        profile["wind_protection_need"] = 0.4


    if apparent_temperature >= 85:
        profile["breathability_need"] = 1.0
    elif apparent_temperature >= 75:
        profile["breathability_need"] = 0.8
    elif apparent_temperature >= 65:
        profile["breathability_need"] = 0.5
    else:
        profile["breathability_need"] = 0.2

    return profile

