from ..proactive_plugin import ProactivePlugin

class HealthPlugin(ProactivePlugin):
    def __init__(self):
        self.sleep_scores = [70, 80, 65, 72, 88, 54, 90]
        self.resting_heart_rates = [65, 60, 70, 65, 60, 55, 65]
        self.active_calories_burnt = [200, 250, 100, 200, 230, 340, 190]
        self.steps = [4000, 6000, 1000, 4200, 6500, 9000, 3900]
        self.future_weather_forecast = ['Rainy', 'Sunny', 'Cloudy', 'Storm and flash flood warning', 'Sunny', 'Hot and humid']
    
    def invoke(self, event):
        output = "Health stats for the past week\n"
        output = output+ "\nSleep scores out of 100 for the past week: "+str(self.sleep_scores)
        output = output+ "\nActive calories burnt over the past week: "+str(self.active_calories_burnt)
        output = output+ "\nStep count over the past week: "+str(self.steps)
        output = output+"\n This is the weather forecast for the upcoming week: "+str(self.future_weather_forecast)
        return output