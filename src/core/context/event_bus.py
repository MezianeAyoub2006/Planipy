import src.core as core

class EventBus:
    def __init__(self, context : core.Context):
        self.context = context 
        self.content = []
       
    def clear(self):
        self.content.clear()

    def push(self, type, **properties):
        self.content.append({
            "type" : type
        } | properties)
        