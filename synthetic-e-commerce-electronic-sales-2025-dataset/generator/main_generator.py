from datetime import date
from faker import Faker
import pandas as pd
import numpy as np
from src import generator_methods as gm

def main() -> None:

    product_prices: dict[str, int] = {
    "Laptop Pro 15": 1299.99, "Desktop PC Gamer": 1549.50, "MacBook Air M2": 1199.00, 
    "Chromebook 14": 299.99, "Gaming Motherboard": 249.00, "Graphics Card RTX 3080": 699.99, 
    "Internal SSD 1TB": 89.99, "DDR4 RAM 16GB": 55.00, "CPU Cooler": 45.00, 
    "Power Supply 750W": 110.00, "PC Case ATX": 95.00, "External Hard Drive 2TB": 65.00, 
    "USB-C Hub": 35.00, "Thermal Paste": 9.99, "Sound Card": 79.00,
    "Wireless Headphones": 199.00, "Noise Cancelling Earbuds": 249.99, "Bluetooth Speaker": 129.00, 
    "Soundbar 5.1": 399.00, "Studio Microphone": 150.00, "Turntable Vinyl Player": 220.00, 
    "Home Theater System": 899.00, "Gaming Headset": 89.00, "Portable MP3 Player": 45.00, 
    "Audio Interface": 160.00, "Wired Earphones": 25.00, "Smart Speaker": 99.00, 
    "Wireless Earbuds Case": 29.99, "Boombox": 75.00, "DJ Controller": 350.00,
    "Smartphone flagship": 999.00, "Budget Smartphone": 199.00, "Smartwatch Series 7": 399.00, 
    "Fitness Tracker": 49.99, "Tablet 10-inch": 329.00, "E-book Reader": 139.00, 
    "Power Bank 20000mAh": 45.00, "Wireless Charger": 30.00, "Smartphone Case": 15.00, 
    "Foldable Phone": 1799.00, "Stylus Pen": 89.00, "VR Headset": 499.00, 
    "Smart Ring": 299.00, "GPS Navigator": 120.00, "Portable Gaming Console": 349.00,
    "DSLR Camera": 850.00, "Mirrorless Camera": 1200.00, "Action Camera 4K": 349.99, 
    "Digital Photo Frame": 60.00, "Camera Lens 50mm": 200.00, "Tripod Stand": 45.00, 
    "Camera Bag": 55.00, "Ring Light": 35.00, "Drone with Camera": 799.00, 
    "Dash Cam": 89.00, "Security Camera WiFi": 120.00, "Photo Printer": 149.00, 
    "Video Camcorder": 550.00, "External Flash": 110.00, "Binoculars": 75.00,
    "Smart TV 55-inch": 599.00, "OLED Monitor 27-inch": 849.00, "4K Projector": 1100.00, 
    "Streaming Stick": 49.99, "Blu-ray Player": 99.00, "Universal Remote": 25.00, 
    "LED Backlight Strip": 19.99, "HDMI Cable 2.1": 15.00, "TV Wall Mount": 40.00, 
    "Antenna Signal Booster": 30.00,
    "Smart Light Bulb": 12.99, "WiFi Router 6": 180.00, "Mesh WiFi System": 299.00, 
    "Smart Thermostat": 220.00, "Video Doorbell": 150.00, "Smart Plug": 18.00, 
    "Robot Vacuum Cleaner": 350.00, "Digital Scale": 25.00, "Electric Toothbrush": 79.00, 
    "Laser Printer": 199.00, "Document Scanner": 130.00, "Paper Shredder": 65.00, 
    "Ergonomic Keyboard": 110.00, "Wireless Mouse": 45.00, "Webcam 1080p": 69.00, 
    "Graphics Tablet": 250.00, "Monitor Arm": 80.00, "Microphone Boom Arm": 45.00, 
    "Office Desk Lamp": 35.00, "Air Purifier": 180.00,
    "Gaming Controller": 59.99, "Mechanical Keyboard": 129.00, "RGB Mousepad": 25.00, 
    "Racing Wheel": 280.00, "Joystick": 65.00, "Gaming Chair": 250.00, 
    "VR Motion Controllers": 120.00, "Console Charging Dock": 25.00, "Capture Card": 170.00, 
    "Retro Console": 89.00, "Handheld Console": 199.00, "Gaming Earbuds": 79.00, 
    "Cooling Pad for Laptop": 30.00, "Cable Management Kit": 15.00, "Headphone Stand": 20.00
    }

    country_configs: list[tuple[str, str, int]] = [
    ("en_IN", "India", 1000),
    ("en_US", "USA", 1200),
    ("de_DE", "Germany", 800),
    ("en_GB", "Great Britain", 900),
    ("fr_FR", "France", 700),
    ("pl_PL", "Poland", 600),
    ("es_ES", "Spain", 650),
    ("it_IT", "Italy", 750),
    ("nl_NL", "Netherlands", 600),
    ("pt_PT", "Portugal", 720),
    ("de_AT", "Austria", 560),
    ("sv_SE", "Sweden", 650),
    ("nl_BE", "Belgium", 650),
    ("cs_CZ", "Czech Republic", 550),
    ("sk_SK", "Slovakia", 500)
    ]

    df_list: list[pd.DataFrame] = []
    for locale, country, amount in country_configs:
        df_list.append(gm.generate_data(
            amount, 
            locale, 
            country, 
            product_prices

        ))

    df: pd.DataFrame = pd.concat(df_list)

    print(df.sample(10))
    # df.to_csv("../data/e_commerce_dataset_2025.csv", index=False, encoding="utf-8")

if __name__ == "__main__":
    main()




