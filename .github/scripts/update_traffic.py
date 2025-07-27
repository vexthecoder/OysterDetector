import requests
import datetime
import os

REPO = "vexthecoder/OysterDetector"
TOKEN = os.getenv("GH_TRAFFIC_TOKEN")
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

def get_json(endpoint):
    url = f"https://api.github.com/repos/{REPO}/{endpoint}"
    response = requests.get(url, headers=HEADERS)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print(f"Response: {response.text}")
        return {}
    return response.json()

views = get_json("traffic/views")
clones = get_json("traffic/clones")

view_count = views.get("count", 0)
unique_visitors = views.get("uniques", 0)
clone_count = clones.get("count", 0)
unique_cloners = clones.get("uniques", 0)

with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

start_marker = "<!--TRAFFIC-STATS-START-->"
end_marker = "<!--TRAFFIC-STATS-END-->"
stats = f"""
**GitHub Repo Stats (last 14 days)**  
🧍 Unique Visitors: {unique_visitors}  
👁️ Total Views: {view_count}  
📥 Unique Cloners: {unique_cloners}  
🔁 Total Clones: {clone_count}  
⏱️ Updated: {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}
"""

new_lines = []
inside_block = False
for line in lines:
    if start_marker in line:
        new_lines.append(line)
        new_lines.append(stats + "\n")
        inside_block = True
    elif end_marker in line:
        new_lines.append(line)
        inside_block = False
    elif not inside_block:
        new_lines.append(line)

with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(new_lines)
