import requests
from bs4 import BeautifulSoup

def scrape_pccoe():
    url = 'https://pccoepune.com'  # Replace with the actual URL of PCCOE
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract admission details
        admission_info = soup.find('div', {'id': 'admission_section'}).text.strip()

        # Extract scholarship info
        scholarship_info = soup.find('div', {'id': 'scholarship_section'}).text.strip()

        # Extract course details
        course_info = soup.find('div', {'id': 'course_section'}).text.strip()

        return {
            "admissions": admission_info,
            "scholarships": scholarship_info,
            "courses": course_info
        }
    else:
        return {"error": "Failed to retrieve information from the website."}
