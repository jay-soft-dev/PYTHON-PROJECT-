
# 1. String Variables (Text Data)
laptop_brand = "Samsung"
model_name = "Galaxy Book4"
processor = "Intel Core 5 120U"
os_version = "Windows 11 Home"

# 2. Integer Variables (Whole Numbers)
ram_gb = 16
ssd_storage_gb = 512
battery_cycles = 45

# 3. Float Variables (Decimal Numbers)
display_size_inches = 15.6
battery_health_percentage = 98.5
cpu_clock_speed_ghz = 3.5

# 4. Boolean Variables (True / False)
has_ssd =   True
is_charging = True
is_battery_saver_on = False

# 5. Calculation using Float & Int Variables
available_storage_gb = ssd_storage_gb - 120  # Subtracting OS and System reserve storage

# 6. Displaying Laptop Details Output
print("==================================================")
print("          LAPTOP SYSTEM INFORMATION               ")
print("==================================================")
print(" Device Name  :", laptop_brand, model_name)
print(" Processor    :", processor)
print(" Operating System :", os_version)
print(" Display Size  :", display_size_inches, "inches")
print("--------------------------------------------------")
print(" RAM Memory :", ram_gb, "GB")
print(" Total SSD Storage :",   ssd_storage_gb, "GB")
print(" Free Storage Left :", available_storage_gb, "GB")
print(" CPU Speed        :", cpu_clock_speed_ghz, "GHz")
print("--------------------------------------------------")
print(" Battery Health :", battery_health_percentage, "%")
print(" Charging Connected:", is_charging)
print(" SSD Installed  :", has_ssd)
print("==================================================")

# 7. Data Types Verification
print("\n--- Verifying Data Types of Variables ---")
print("laptop_brand type :", type(laptop_brand))
print("ram_gb type :",     type(ram_gb))
print("battery_health type:",type(battery_health_percentage))
print("is_charging type :",  type(is_charging))
print("==================================================")