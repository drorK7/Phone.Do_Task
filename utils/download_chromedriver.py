import requests
from zipfile import ZipFile
import io
import os

def download_latest_chromedriver(output_folder):
    # Define the URL for the latest chromedriver release
    chromedriver_url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"

    # Get the latest release version
    response = requests.get(chromedriver_url)
    version_number = response.text.strip()

    # Construct the download URL
    download_url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/win32/chromedriver-win32.zip"

    # Define the download path
    download_path = os.path.join(output_folder, "chromedriver_win32.zip")

    # Download the chromedriver zip file
    response = requests.get(download_url)
    with open(download_path, 'wb') as zip_file:
        zip_file.write(response.content)

    # Extract only the chromedriver.exe to the output folder
    with ZipFile(download_path, 'r') as zip_ref:
        chromedriver_file = [name for name in zip_ref.namelist() if "chromedriver.exe" in name][0]
        zip_ref.extract(chromedriver_file, output_folder)

    # Delete the zip file
    os.remove(download_path)

    # Rename the extracted file to chromedriver.exe
    new_chromedriver_path = os.path.join(output_folder, "chromedriver.exe")
    os.rename(os.path.join(output_folder, chromedriver_file), new_chromedriver_path)

    print(f"Latest Chromedriver {version_number} downloaded and extracted to {new_chromedriver_path} successfully.")

if __name__ == "__main__":
    # Specify the output folder where chromedriver will be saved
    drivers_folder = os.path.abspath("../selenium_Python/drivers")

    # Create the drivers folder if it doesn't exist
    os.makedirs(drivers_folder, exist_ok=True)

    # Download the latest chromedriver to the specified folder
    download_latest_chromedriver(drivers_folder)
