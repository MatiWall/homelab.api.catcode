class EventBus:
    def __init__(self):
        self.subscriptions = {}

    def subscribe(self, event_type, handler):
        if event_type not in self.subscriptions:
            self.subscriptions[event_type] = []
        self.subscriptions[event_type].append(handler)

    async def publish(self, event):
        handlers = self.subscriptions.get(event.type, [])
        for handler in handlers:
            await handler(event)