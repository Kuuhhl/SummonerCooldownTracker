import requests
import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
LOCALE = "en_US"


def get_allgamedata_api_response():
    return requests.get(
        "https://127.0.0.1:2999/liveclientdata/allgamedata", verify=False
    ).json()


def get_activeplayer_name():
    return requests.get(
        "https://127.0.0.1:2999/liveclientdata/activeplayer", verify=False
    ).json()["summonerName"]


def get_all_champions_ingame_data():
    response = get_allgamedata_api_response()["allPlayers"]

    return [
        {
            "summonerName": response[x]["summonerName"],
            "championName": response[x]["championName"],
            "spells": [
                response[x]["summonerSpells"]["summonerSpellOne"]["displayName"],
                response[x]["summonerSpells"]["summonerSpellTwo"]["displayName"],
            ],
            "items": response[x]["items"],
            "team": response[x]["team"],
        }
        for x in range(len(response))
    ]


def get_team(summonerName):
    response = get_all_champions_ingame_data()
    return [
        response[x]["team"]
        for x in range(len(response))
        if response[x]["summonerName"] == summonerName
    ][0]


def get_enemy_champions_ingame_data():
    response = get_all_champions_ingame_data()
    return [
        response[x]
        for x in range(len(response))
        if response[x]["team"] != get_team(get_activeplayer_name())
    ]


def get_level(champion):
    response = get_allgamedata_api_response()["allPlayers"]
    return [
        response[x]["level"]
        for x in range(len(response))
        if response[x]["championName"] == champion
    ][0]


def get_summoner(champion):
    response = get_enemy_champions_ingame_data()
    return [
        response[x]["spells"]
        for x in range(len(response))
        if response[x]["championName"] == champion
    ][0]


def get_all_summoner_cooldowns():
    with requests.get(
        "https://ddragon.leagueoflegends.com/cdn/"
        + str(get_latest_patch())
        + "/data/"
        + LOCALE
        + "/summoner.json"
    ) as response:
        response = response.json()
        return [
            {
                "name": response["data"][spell]["name"],
                "cooldown": response["data"][spell]["cooldown"][0],
            }
            for spell in response["data"]
        ]


def get_latest_patch():
    with requests.get(
        "https://ddragon.leagueoflegends.com/api/versions.json"
    ) as response:
        return response.json()[0]


def get_cooldown(champion, summonerspell):
    if summonerspell == "Teleport":
        return 430.58823529412 - 10.588235294118 * get_level(champion)
    response = get_all_summoner_cooldowns()
    return int(
        [
            response[x]["cooldown"]
            for x in range(len(response))
            if response[x]["name"] == summonerspell
        ][0]
    )


def get_current_time():
    return get_allgamedata_api_response()["gameData"]["gameTime"]


pprint.PrettyPrinter(indent=4).pprint(get_current_time())
