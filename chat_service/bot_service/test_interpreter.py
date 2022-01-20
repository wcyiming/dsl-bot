import  pytest
import parser as parser
from classes import State
from interpreter import generate
path = "script\\script.txt"

def test_load():
    with open(path, 'r', encoding='utf8') as f:
        script = parser.load_script(f)

    #test generate in different states
    test = []
    test.append(1)
    test.append(script[2].reply)
    assert generate(script,0,"steam") == test
    test.clear()
    test.append(2)
    test.append(script[3].reply)
    assert generate(script,1,"buy") == test
    test.clear()
    test.append(4)
    test.append(script[5].reply)
    assert generate(script,0,"epic") == test
    test.clear()
    test.append(6)
    test.append(script[9])
    assert generate(script,6,"edfgsdfg") == test
    #test wrong state
    test.clear()
    test.append(0)
    test.append(script[9])
    assert generate(script,114514,"edfgsdfg") == test