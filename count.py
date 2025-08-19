import requests
import datetime

# === CONFIG ===
API_TOKEN = "bJqIsL-M1xqbsiX6sO659e4s7A6Ef-wA09FvLVbv"
ZONE_TAG = "8f1267309af6f1feaf406e284dcf72aa"
API_URL = "https://api.cloudflare.com/client/v4/graphql"

def get_total_unique_visitors():
    start_date = "2025-08-05"
    end_date = datetime.date.today().strftime("%Y-%m-%d")  # today

    # === GraphQL QUERY ===
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
