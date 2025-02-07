
from typing import List, Optional
from pydantic import BaseModel, Field
from langchain.tools import tool
from datetime import datetime

service = None


def init_calendar_service(calendar_service) -> None:
    """Initialize the calendar service globally"""
    global service
    service = calendar_service

@tool
def get_time(input: str = None) -> List[str]:
    """Returns the current day of the week and thecurrent date, useful tool to get anything time related
    First elemenet is the current day of the week and the second element is the current date and time
    Use this tool to calculate the from_where parameter for get_events tool and find out the date or day of the week"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    day_of_week = datetime.now().strftime("%A")  # Get the full weekday name
    return [day_of_week, current_time]

@tool
def get_events(num: int, from_where: str):
    """Returns {num} events, for each event it returns its ID, and its details starting from from_where date
        from_where should be given in RFC3339 format + "Z" at the end,
        from_where is the day from which the events should be fetched
        from_where should be calculated with help of get_time tool"""
    event_result = service.events().list(calendarId="primary", timeMin=from_where, maxResults = num, singleEvents=True, orderBy="startTime").execute()
    events = event_result.get("items", [])

    if not events:
        print("No upcoming events found!")
        return 0
    result = []
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("data"))
        end = event["end"].get("dateTime", event["end"].get("data"))
        summary = event.get("summary", "No Summary")
        event_id = event.get("id", "No ID")  
        result.append({"id": event_id, "start": start, "end": end, "summary": summary, "summary": summary})
        
    return result


class EventInput(BaseModel):
    """input for set_event"""
    summary: str = Field(..., description="Summary of the event")
    description: str = Field(..., description="Description of the event")
    start_time: Optional[str] = Field(..., description="Start time of the event, must be in RFC3339 format for example, 2011-06-03T10:00:00")
    end_time: Optional[str] = Field(..., description="End time of the event, must be in RFC3339 format, for example, 2011-06-03T11:00:00")

@tool(args_schema=EventInput)
def set_event(summary: str = None, description: str = None, start_time: str = None, end_time: str = None) -> None:
    """Creates and sets an event based on input, input should be given as ab object with keys: summary, description, start_time, end_time, variables names in string format
    time variables should be given in RFC3339 format
    """
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_time,
            'timeZone': 'Europe/London',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Europe/London',
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))

@tool
def delete_event(event_id: str) -> str:
    """
    Deletes an event from the user's Google Calendar using the provided event ID.
    Calls "{get_events}" tool to get the event ID of the event to be deleted.
    Parameters: event_id (str): The ID of the event to delete.
    Returns: str: A confirmation message if the event is deleted successfully, or an error message if the operation fails.
    """

    service.events().delete(calendarId="primary", eventId=event_id).execute()

    # Return a confirmation message
    return f"Event with ID '{event_id}' has been successfully deleted."

    
    