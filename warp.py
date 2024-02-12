import tkinter as tk
from collections import defaultdict
from string import ascii_uppercase

class App:
    def __init__(self, title="Untitled Window", x=130, y=130):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{x}x{y}")
        self.widgets = {}  # Dictionary to store widgets by ID
        self.widget_counters = defaultdict(int)  # Default dictionary to store widget count
        self.create = self.Create(self)

    def getwidlist(self):
        return self.widgets

    def getwid(self, id):
        return self.widgets.get(id)

    def run(self):
        self.root.mainloop()

    class Create:
        def __init__(self, app):
            self.app = app

        def _generate_id(self, prefix):
            # Increment the count for the widget type
            self.app.widget_counters[prefix] += 1
            # Generate an ID like "L1", "B2", etc.
            return f"{prefix}{self.app.widget_counters[prefix]}"

        def label(self, text="Untitled Label", id=None, **options):
            if id is None:
                id = self._generate_id('L')
            label = tk.Label(self.app.root, text=text, **options)
            label.pack()
            self.app.widgets[id] = label
            return id

        def button(self, text="Untitled Button", id=None, **options):
            if id is None:
                id = self._generate_id('B')
            button = tk.Button(self.app.root, text=text, **options)
            button.pack()
            self.app.widgets[id] = button
            return id

        def entry(self, id=None, **options):
            if id is None:
                id = self._generate_id('E')
            entry = tk.Entry(self.app.root, **options)
            entry.pack()
            self.app.widgets[id] = entry
            return id

        def dropdown(self, selected_choice="", options=[], id=None, **other):
            if id is None:
                id = self._generate_id('D')
            selected_choice = tk.StringVar(self.app.root)
            selected_choice.set(selected_choice)
            dropdown = tk.OptionMenu(self.app.root, selected_choice, *options, **other)
            dropdown.pack()
            self.app.widgets[id] = dropdown
            return id

        def checkbox(self, text="", id=None, **options):
            if id is None:
                id = self._generate_id('C')
            var = tk.BooleanVar(self.app.root)
            checkbox = tk.Checkbutton(self.app.root, text=text, variable=var, **options)
            checkbox.pack()
            self.app.widgets[id] = checkbox
            self.app.widgets[f"{id}_var"] = var
            return id
