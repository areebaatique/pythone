import asyncio
from typing import Protocol, Type, Dict, List, runtime_checkable


# -------- Event Base Class --------

class Event:
    pass


class UserLoggedInEvent(Event):
    def __init__(self, username: str):
        self.username = username


class DataUpdatedEvent(Event):
    def __init__(self, data_id: int):
        self.data_id = data_id


# -------- EventHandler Protocol --------

@runtime_checkable
class EventHandler(Protocol):
    async def handle(self, event: Event) -> None:
        ...


# -------- EventBus --------

class EventBus:
    def __init__(self):
        self._handlers: Dict[Type[Event], List[EventHandler]] = {}

    def register(self, event_type: Type[Event], handler: EventHandler):
        self._handlers.setdefault(event_type, []).append(handler)

    async def publish(self, event: Event):
        event_type = type(event)
        handlers = self._handlers.get(event_type, [])
        for handler in handlers:
            try:
                await handler.handle(event)
            except Exception as e:
                print(f"Error handling {event_type.__name__}: {e}")


# -------- Sample Handlers --------

class LoggingHandler:
    async def handle(self, event: Event):
        print(f"[LOG] Received event: {event.__class__.__name__}")

class EmailNotificationHandler:
    async def handle(self, event: Event):
        if isinstance(event, UserLoggedInEvent):
            print(f"[EMAIL] Welcome email sent to {event.username}")

class PopupAlertHandler:
    async def handle(self, event: Event):
        if isinstance(event, UserLoggedInEvent):
            print(f"[POPUP] User {event.username} logged in!")


# -------- Example Main --------

async def main():
    bus = EventBus()
    
    # Register handlers
    bus.register(UserLoggedInEvent, LoggingHandler())
    bus.register(UserLoggedInEvent, EmailNotificationHandler())
    bus.register(UserLoggedInEvent, PopupAlertHandler())

    # Publish an event
    await bus.publish(UserLoggedInEvent("areeba"))


if __name__ == "__main__":
    asyncio.run(main())
