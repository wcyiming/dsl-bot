"""the module to analyse the request and build response with formatted script

Recieve formatted script,client's state,client's request text
check the script and build response with next client'id and reply text 

Typical usage example:
result = generate(script,0,"hello_world")
"""
from classes import State

def generate(script,state_id,request):
    """ build response with formatted script and return
    
    Check state_id and request in the Script table and the event of aimed script
    If the aimed script has the key, get key's value and get state[value]'s reply 
    If not,return the default reply.
    Offered state_id check to insure the security.
    
    Args:
        script (list[State,str]): list of script States and a default reply string
        state_id (int): received id from client which stands for client's id currently
        request (str): received text from client which is client's entry
    
    Returns:
        list[int,str]: next state id client goto and bot's reply
    """ 
    answer = []
    i = 0
    nowid = 0
    for tmp in script:                            #the sequence of Script is not the Script's id
        if isinstance(tmp,State):            
            if tmp.id == state_id:
                nowid = i
                break
        i = i + 1
    if request in script[nowid].event:        
        answer.append(script[nowid].event[request])
        toid = 0
        j = 0
        for tmp in script:
            if isinstance(tmp,State):
                if tmp.id == script[nowid].event[request]:
                    toid = j
                    break
            j = j + 1
        answer.append(script[toid].reply)
    else :
        if state_id > len(script):
            state_id = 0
        answer.append(state_id)
        for tmp in script:
            if isinstance(tmp,str):
                answer.append(tmp)
                break
    return answer