from bs4 import BeautifulSoup
import requests

def listGuildMembers(guild_name: str, region: str):
    url = f"https://www.naeu.playblackdesert.com/en-US/Adventure/Guild/GuildProfile?guildName={guild_name}&region={region.upper()}"
    guild_page = requests.get(url)
    soup = BeautifulSoup(guild_page.content, "html.parser")
    res = soup.find(class_="container guild_profile")
    
    if res is None:
        raise ValueError
    
    members = res.find_all("a")
    guild_member_list = []
    for i in members[1:]:
        guild_member_list.append(i.text)
    
    return guild_member_list


if __name__ == "__main__":
    print(listGuildMembers("name", "na")) # example

# for naeu only
# for other regions, change url to your desired region