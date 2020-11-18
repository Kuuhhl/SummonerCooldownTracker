from PIL import ImageGrab, Image, ImageOps, ImageEnhance
import pytesseract
import datetime
import requests
import json
import keyboard
import sys


def add_time(timestamp, seconds):
    timestamp = datetime.datetime.strptime(timestamp, "%M:%S")
    newtimestamp = timestamp + datetime.timedelta(seconds=seconds)
    return newtimestamp


def get_combos():
    # CONFIG
    fullcombo = 215.0
    wqcombo = 115.0

    r = json.loads(
        requests.get(
            "https://127.0.0.1:2999/liveclientdata/activeplayer", verify=False
        ).text
    )
    mana = r["championStats"]["resourceValue"]
    print("Full Combos available: " + str(int(mana / fullcombo)))
    print("W-Q Combos available: " + str(int(mana / wqcombo)))


def get_level(champion):
    r = json.loads(
        requests.get(
            "https://127.0.0.1:2999/liveclientdata/allgamedata", verify=False
        ).text
    )
    for x in range(len(r)):
        if r[x]["championName"] == champion:
            return r[x]["level"]


def get_summoner():
    im = ImageEnhance.Contrast(
        ImageOps.invert(ImageGrab.grab(bbox=(0, 1354, 294, 1370)).convert("L"))
    ).enhance(4.0)
    text = pytesseract.image_to_string(im).split("\n")[0]
    print(text)
    timestamp = text.split(" ")[0].replace("[", "").replace("]", "")
    champion = text.split(" ")[3]
    spell = text.split(" ")[4]
    if spell == "Flash":
        newtime = add_time(timestamp, 300)
        print(
            champion
            + " does'nt have "
            + spell
            + " until "
            + str(newtime.minute)
            + " minutes and "
            + str(newtime.second)
            + " seconds."
        )
    elif spell == "Teleport":
        newtime = add_time(timestamp, (430.588 - 10.588 * get_level(champion)))
        print(
            champion
            + " does'nt have "
            + spell
            + " until "
            + str(newtime.minute)
            + " minutes and "
            + str(newtime.second)
            + " seconds."
        )
    elif spell == "Ignite" or spell == "Barrier":
        newtime = add_time(timestamp, 180)
        print(
            champion
            + " does'nt have "
            + spell
            + " until "
            + str(newtime.minute)
            + " minutes and "
            + str(newtime.second)
            + " seconds."
        )
    elif spell == "Ghost" or spell == "Exhaust" or spell == "Cleanse":
        newtime = add_time(timestamp, 210)
        print(
            champion
            + " does'nt have "
            + spell
            + " until "
            + str(newtime.minute)
            + " minutes and "
            + str(newtime.second)
            + " seconds."
        )
    else:
        print("Unknown spell or other error")


keyboard.add_hotkey("z", get_summoner)
