from models.event import *
import datetime


event1 = Event(datetime.date(2022, 10, 8), "birthday party", 16, "hyde park", "murder mystery")
event2 = Event(datetime.date(2022, 11, 8), "work meeting", 8, "the barn",  "sales targest")
event3 = Event(datetime.date(2022, 12, 22), "nasa lunch", 800, "washington park", "artimis 1")

events = [event1, event2, event3]

def add_event(new_event):
    events.append(new_event)