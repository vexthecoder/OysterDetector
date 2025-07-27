import requests, datetime

REPO = "vexthecoder/OysterDetector"
TOKEN = "${{ secrets.GH_TRAFFIC_TOKEN }}"
HEADERS = {"Authorization": f"token {TOKEN}"}

def get_json(endpoint):
    r = requests.get(f"https://api.github.com/repos/{REPO}/{endpoint}", headers=HEADERS)
    return r.json()

views = get_json("traffic/views")
clones = get_json("traffic/clones")

with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

start_marker = "<!--TRAFFIC-STATS-START-->"
end_marker = "<!--TRAFFIC-STATS-END-->"
stats = f"""
**GitHub Repo Stats (last 14 days)**  
🧍 Unique Visitors: {views['uniques']}  
👁️ Total Views: {views['count']}  
📥 Unique Cloners: {clones['uniques']}  
🔁 Total Clones: {clones['count']}  
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
