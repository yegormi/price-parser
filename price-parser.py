import requests
from bs4 import BeautifulSoup
import time

# Define the URL of the website
url = "https://touch.com.ua/item/apple-macbook-air-13-retina-m2-8-core-cpu-10-core-gpu-16-core-neural-engine-8gb-ram-512gb-ssd-starli_1/"
# Define the initial price
old_price = None

is_debug = False
is_price_shown = True

while True:
    try:
        # Send an HTTP GET request to the website
        response = requests.get(url)
        if is_debug:
            print("Sent HTTP request")

        # Check if the request was successful
        if response.status_code == 200:
            if is_debug:
                print("HTTP request is successful")
                # Parse the HTML content of the page

            soup = BeautifulSoup(response.text, 'html.parser')
            if is_debug:
                print("HTML page is parsed")

            # Find the element that contains the price
            price_element = soup.find('a', class_='price changePrice')
            if is_debug:
                print("Found the price element")

            if price_element:
                # Extract the current price (assuming it's in the format "63 139 ₴")
                current_price = int(price_element.text.strip().replace('₴', '').replace(' ', ''))
                if is_debug:
                    print("The price is extracted")

                # Check if the price has changed
                if old_price is None:
                    # First time checking, set the old price
                    old_price = current_price
                elif current_price == old_price:
                    # Price hasn't changed, send a notification or message to yourself
                    if is_price_shown:
                        print(f"Not changed: {current_price} ₴")
                elif current_price != old_price:
                    old_price = current_price
                    # Price has changed, send a notification or message to yourself
                    if is_debug:
                        print(f"-> -> Price is changed from {old_price} ₴ to {current_price} ₴")
                        break
            else:
                print("Price element not found on the page.")
        else:
            print("Failed to fetch the webpage. Check your internet connection or the URL.")

        # Wait for an hour before checking again (3600 seconds)
        time.sleep()
    except KeyboardInterrupt:
        # Exit the loop if the user interrupts (e.g., Ctrl+C)
        break