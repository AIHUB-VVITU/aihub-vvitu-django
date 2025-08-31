import requests
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Access variables
API_TOKEN = os.getenv("API_TOKEN")
ZONE_TAG = os.getenv("ZONE_TAG")
API_URL = os.getenv("API_URL")

def get_total_unique_visitors():
    start_date = "2025-08-05"
    end_date = datetime.date.today().strftime("%Y-%m-%d") 

    query = """
    {
      viewer {
        zones(filter: {zoneTag: "%s"}) {
          httpRequests1dGroups(
            filter: { date_geq: "%s", date_leq: "%s" }
            limit: 100
          ) {
            dimensions {
              date
            }
            uniq {
              uniques
            }
          }
        }
      }
    }
    """ % (ZONE_TAG, start_date, end_date)

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, headers=headers, json={"query": query})

    total_unique_visitors = 0

    if response.status_code == 200:
        data = response.json()
        try:
            results = data["data"]["viewer"]["zones"][0]["httpRequests1dGroups"]
            for entry in results:
                uniques = entry["uniq"]["uniques"]
                total_unique_visitors += uniques
        except Exception as e:
            print("⚠️ Error parsing response:", e)
            print(data)
    else:
        print("❌ Request failed:", response.status_code, response.text)

    return total_unique_visitors
