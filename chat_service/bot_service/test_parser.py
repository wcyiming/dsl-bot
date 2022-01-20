import  pytest
from parser import load_script
from classes import State
path = "script\\script.txt"

def test_load():
    with open(path, 'r', encoding='utf8') as f:
        script = load_script(f)
    #test script type
    assert script is not None
    assert isinstance(script[8], State)
    assert isinstance(script[1], State)
    assert isinstance(script[2], State)
    assert isinstance(script[3], State)
    assert isinstance(script[4], State)
    assert isinstance(script[5], State)
    assert isinstance(script[6], State)
    assert isinstance(script[7], State)
    assert isinstance(script[9], str)
    #test script content
    assert script[1].id == 0
    assert script[1].event['steam'] == 1
    assert script[1].event['epic'] == 4
    assert script[1].event['origin'] == 6
    assert script[1].event['uplay'] == 7
    assert script[2].event['buy'] == 2
    assert script[2].event['search'] == 3
    assert script[2].event['back'] == 0
    assert script[3].event['back'] == 0
    assert script[4].event['back'] == 0
    assert script[5].event['free'] == 5
    assert script[5].event['back'] == 0
    assert script[6].event['back'] == 0
    assert script[3].reply == ("https://store.steampowered.com\n"
    "you can search the game you want and buy it in this website\n"
    "enter: \"back\" to return to the menu\n")


"""fo = open("foo.txt", "w")
fo.write()
"""