import time  # For adding delays
import requests
import uagent  # Replace with the actual uAgent library import

API_KEY = "your_openweathermap_api_key"

# Define a function to fetch temperature data from a weather API
def fetch_temperature(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            current_temp = data['main']['temp']
            return current_temp
        else:
            print(f"Error fetching data: {data['message']}")
            return None
    except Exception as e:
        print(f"Error fetching data: {str(e)}")
        return None

# Define a function to check temperature alerts and send notifications
def check_temperature_alert(location, min_temp, max_temp):
    current_temp = fetch_temperature(location)

    if current_temp < min_temp:
        send_alert(f"Temperature Alert: It's too cold ({current_temp}°C) in {location}!")

    if current_temp > max_temp:
        send_alert(f"Temperature Alert: It's too hot ({current_temp}°C) in {location}!")

# Define a function to send alerts or notifications (e.g., via email, SMS, or push notification)
def send_alert(message):
    # Implement alert/notification logic here
    # Replace this with the actual notification method you plan to use

    print(f"Sending Alert: {message}")

# Main function
def main():
    location = input("Enter your preferred location: ")
    min_temp = float(input("Enter the minimum temperature threshold (in °C): "))
    max_temp = float(input("Enter the maximum temperature threshold (in °C): "))

    while True:
        check_temperature_alert(location, min_temp, max_temp)
        # Add a delay between temperature checks (e.g., every 30 minutes)
        time.sleep(1800)  # 1800 seconds = 30 minutes

if __name__ == "__main__":
    main()
