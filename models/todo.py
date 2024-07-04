class Todo:
    def __init__(self, text, status='todo', done=False):
        self.text = text
        self.status = status
        self.done = done

    def toggle_done(self):
        self.done = not self.done
