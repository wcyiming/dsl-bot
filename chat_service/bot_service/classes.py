"""the module to store thing will be global used

Powered by Python,this module defines a class to store the script
in global enviroment. This module shouldn't import any thing from
program to avoid circular import

Typical usage example:
state = State(0)
"""
class State:
    """ this class using to store the states read from the script

    This class is used by any module who need to use the content
    from the script.It will help to store and read different data
    directly.

    Attributes:
        reply:the text the bot need to reply to customers
        id:the id of the state.the id of state 0 is 0
        event:a dict to store events.It's struct is {test_string : state_id }
        test_string: the test of customer's request
        state_id: next state jump to
    """
    def __init__(self, id):
        """Inits StateClass with id"""
        self.id = id
        self.event = dict()
        self.reply = "please enter reply in script"
    
    def add(self,key,id):
        """Add test_string : state_id to the event dict"""
        self.event[key] = id