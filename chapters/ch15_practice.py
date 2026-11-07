# Python book chapter 15, worked practice
class EmailNotifier:
    def notify(self, message):
        return f"email: {message}"

class LogNotifier:
    def notify(self, message):
        return f"log: {message}"

def dispatch(notifiers, message):
    return [n.notify(message) for n in notifiers]

print(dispatch([EmailNotifier(), LogNotifier()], "سلام"))
