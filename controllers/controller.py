from flask import render_template, request, redirect
from app import app
from models.event_list import events, add_event
from models.event import Event
import datetime


@app.route("/events")
def index():
    return render_template("index.html", title="Home", events=events)

@app.route("/events", methods=["POST"])
def add_new_event():
    date = request.form["date"]
    split_date = date.split("/")
    date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    room_location = request.form["room_location"]
    event_name = request.form["event_name"]
    description = request.form["description"]
    guest_qty = request.form["guest_qty"]
    new_event = Event(date = date, event_name = event_name, guest_qty = guest_qty, room_location = room_location, description = description)
    add_event(new_event)
    
    return redirect("/events")


