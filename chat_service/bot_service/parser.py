"""the module to parser the script.txt to defined struct

Recieve the file stream and load data from file
parser the data to the struct bot_interpreter can read

Typical usage example:
script = load_script(0)
"""


from typing import IO
from classes import State

def analyze(lines) -> list:
    
    """ Parsing the script.txt, return formatted script structure
    
    First, splint the data read in as lines. Read the head to decide which
    type of the lines stand for.Because of It will check the test if in reply,
    so first check if it's end reply,then will check replyFlag = True,
    which means in reply mode,it will read until the end reply and only add text.
    Then, line title analysis and add the information of different situations to the state structure.
    
    Args:
        lines (list[str]): whole content form script text
    
    Returns:
        list[State,str]: formatted script Classes and default string (list)
    """ 

    result = []
    replyFlag = False
    defaultFlag = False
    tmp = State(-1)
    for line in lines:
        if line[0] == "\n":
            continue
        line_element = line.split()
        if line_element[0] == "end" :                  #check the end before check replyFlag
            if line_element[1] == "reply":
                replyFlag = False
        if replyFlag:                                  #in reply mode
            tmp.reply = tmp.reply + line
        else :
            if line_element[0] == "state" :
                result.append(tmp)
                tmp = State(int(line_element[1]))
            elif line_element[0] == "reply:" :
                replyFlag = True
                text_tmp = line.replace("reply: ","")
                tmp.reply = text_tmp
            elif line_element[0] == "event:" :
                tmp.add(line_element[1],int(line_element[3]))
            elif line_element[0] == "default:" and defaultFlag == False :  #one default is enough
                result.append(tmp)
                text_tmp = line.replace("default: ","")
                result.append(text_tmp)
                defaultFlag = True
    return result

def load_script(f: IO) -> list:
    """parse a script file stream to program readable script

    Args:
        f (IO): fp

    Returns:
        list[State,str]: formatted script Classes and default string (list) 
    """
    lines = f.readlines()
    script = analyze(lines)

    if script is None:
        return None

    return script