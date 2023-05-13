import requests
from bs4 import BeautifulSoup
import json

# REQUEST PART
response = requests.get("http://www.koeri.boun.edu.tr/scripts/lst4.asp")


# SOUP PART
soup = BeautifulSoup(response.content, "html.parser")

fetched_datas = soup.find("pre").text

to_json = {}


earthquakes = fetched_datas.splitlines()[7:-1]
for count, fetched_data in enumerate(earthquakes, start=1):
    fetched_data = fetched_data.split()
    if "İlksel" in fetched_data:
        to_json[count] = {
            "time": {"date": fetched_data[0],
                     "hour": fetched_data[1]
                     },
            "coordinate": {"latitude": float(fetched_data[2]),
                           "longitude": float(fetched_data[3])
                           },
            "depth": float(fetched_data[4]),
            "magnitude": {"MD": fetched_data[5],
                          "ML": fetched_data[6],
                          "MW": fetched_data[7]
                          },
            "location": fetched_data[8:-1],
            "state": fetched_data[-1]
        }
    else:
        to_json[count] = {
            "time": {"date": fetched_data[0],
                     "hour": fetched_data[1]
                     },
            "coordinate": {"latitude": float(fetched_data[2]),
                           "longitude": float(fetched_data[3])
                           },
            "depth": float(fetched_data[4]),
            "magnitude": {"MD": fetched_data[5],
                          "ML": fetched_data[6],
                          "MW": fetched_data[7]
                          },
            "location": fetched_data[8:-3],
            "state": fetched_data[-3:]
        }




with open("earthquakes.json", "w", encoding="utf-8") as file:
    json.dump(to_json, file, ensure_ascii=False, indent=4)
