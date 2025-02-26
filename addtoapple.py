from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager

# Set up Selenium
options = webdriver.ChromeOptions()

options.add_argument("--disable-gpu")  # Disable GPU acceleration
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-extensions")  # Disable extensions
options.add_argument("--disable-images")  # Disable images (may vary by site)
options.add_argument("--window-size=1920x1080")  # Set window size for visibility if needed

options.add_experimental_option("detach", True)  # Keep browser open
driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()), options=options)

# Open Apple Music
driver.get("https://music.apple.com/")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'input')))  # Wait until search box is loaded

# Manually log in to Apple Music before running the script!
input("🔹 Log in to Apple Music, then press Enter to continue...")

# Load songs from file
with open("spotify_liked_songs.txt", "r") as file:
    songs = file.readlines()

for song in songs:
    song = song.strip()

    # Find search bar and enter song name
    search_box = driver.find_element(By.XPATH, "//input[@type='search']")
    search_box.clear()
    search_box.send_keys(song)
    search_box.send_keys(Keys.RETURN)

    try:

        print("Starting try")

        # Wait for the results to load
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='top-search-result']")))

        print("Waited until load")

        # Find the first song result in the grid
        song_box = driver.find_element(By.XPATH, "//div[@data-testid='top-search-result']")
        print("Found song box")

        # Hover over the song box to display the "+" button
        # ActionChains(driver).move_to_element(song_box).perform()
        # time.sleep(0.5)  # Wait briefly for the button to appear

        print("Hover")

        # Click the "+" button (Add to Library)
        add_button = driver.find_element(By.XPATH, "//button[@data-testid='add-to-library-button']")

        print("Found add button")

        add_button.click()
        print(f"✅ Added: {song}")

    except:
        print(f"❌ Could not add: {song}")

    time.sleep(1)  # Pause before searching next song

print("🎉 All songs processed!")
driver.quit()