import datetime
import requests
import re

# 1. Calculate Uptime (Age)
birth_date = datetime.date(2003, 12, 2)
today = datetime.date.today()
age_days = (today - birth_date).days
years = age_days // 365
days = age_days % 365
uptime_string = f"{years}y {days}d"

# 2. Fetch GitHub Data (Replace USERNAME with yours)
username = "bochamaakram"
# Optional: Use a GitHub Token if you hit rate limits
# headers = {"Authorization": "token YOUR_GITHUB_TOKEN"}
user_data = requests.get(f"https://api.github.com/users/{username}").json()

public_repos = user_data.get("public_repos", 95)
followers = user_data.get("followers", 196)

# Note: Total stars and lines of code require iterating through repos, 
# or using the GitHub GraphQL API, but let's stick to basics for representation.

# 3. Read and update the template SVG file (dark_mode.svg contains the base structure in dark colors)
with open("dark_mode.svg", "r", encoding="utf-8") as f:
    template_content = f.read()

# Simple regex replacement using the IDs
updated_content = re.sub(r'id="age_data">[^<]+', f'id="age_data">{uptime_string}', template_content)
updated_content = re.sub(r'id="repo_data">[^<]+', f'id="repo_data">{public_repos}', updated_content)
updated_content = re.sub(r'id="follower_data">[^<]+', f'id="follower_data">{followers}', updated_content)

# Write dark mode SVG file (the template is already in dark colors)
with open("dark_mode.svg", "w", encoding="utf-8") as f:
    f.write(updated_content)

# Convert colors to create the light theme SVG
light_content = updated_content
colors = {
    "#11111b": "#dce0e8",  # Background: Mocha Crust -> Latte Crust
    "#cdd6f4": "#4c4f69",  # Text: Mocha Text -> Latte Text
    "#cba6f7": "#8839ef",  # Key: Mocha Mauve -> Latte Mauve
    "#89b4fa": "#1e66f5",  # Value: Mocha Blue -> Latte Blue
    "#a6e3a1": "#40a02b",  # addColor: Mocha Green -> Latte Green
    "#f38ba8": "#d20f39",  # delColor: Mocha Red -> Latte Red
    "#585b70": "#bcc0cc",  # dots/gray: Mocha Surface2 -> Latte Surface1
}

for dark_color, light_color in colors.items():
    light_content = light_content.replace(dark_color, light_color)

# Write light mode SVG files
with open("profile-card.svg", "w", encoding="utf-8") as f:
    f.write(light_content)

with open("light_mode.svg", "w", encoding="utf-8") as f:
    f.write(light_content)