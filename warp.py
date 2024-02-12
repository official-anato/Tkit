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

        def canvas(self, width=200, height=100, id=None, **options):
            if id is None:
                id = self._generate_id('CN')
            canvas = tk.Canvas(self.app.root, width=width, height=height, **options)
            canvas.pack()
            self.app.widgets[id] = canvas
            return id

        def frame(self, id=None, **options):
            if id is None:
                id = self._generate_id('F')
            frame = tk.Frame(self.app.root, **options)
            frame.pack()
            self.app.widgets[id] = frame
            return id

        def listbox(self, id=None, **options):
            if id is None:
                id = self._generate_id('LB')
            listbox = tk.Listbox(self.app.root, **options)
            listbox.pack()
            self.app.widgets[id] = listbox
            return id

        def menubutton(self, text="Untitled Menubutton", id=None, **options):
            if id is None:
                id = self._generate_id('MB')
            menubutton = tk.Menubutton(self.app.root, text=text, **options)
            menubutton.pack()
            self.app.widgets[id] = menubutton
            return id

        def message(self, text="Untitled Message", id=None, **options):
            if id is None:
                id = self._generate_id('MSG')
            message = tk.Message(self.app.root, text=text, **options)
            message.pack()
            self.app.widgets[id] = message
            return id

        def radiobutton(self, text="Untitled Radiobutton", id=None, **options):
            if id is None:
                id = self._generate_id('RB')
            var = tk.IntVar(self.app.root)
            radiobutton = tk.Radiobutton(self.app.root, text=text, variable=var, **options)
            radiobutton.pack()
            self.app.widgets[id] = radiobutton
            self.app.widgets[f"{id}_var"] = var
            return id

        def scale(self, id=None, **options):
            if id is None:
                id = self._generate_id('S')
            scale = tk.Scale(self.app.root, **options)
            scale.pack()
            self.app.widgets[id] = scale
            return id

        def scrollbar(self, id=None, **options):
            if id is None:
                id = self._generate_id('SC')
            scrollbar = tk.Scrollbar(self.app.root, **options)
            scrollbar.pack()
            self.app.widgets[id] = scrollbar
            return id

        def spinbox(self, id=None, **options):
            if id is None:
                id = self._generate_id('SB')
            spinbox = tk.Spinbox(self.app.root, **options)
            spinbox.pack()
            self.app.widgets[id] = spinbox
            return id

        def text(self, id=None, **options):
            if id is None:
                id = self._generate_id('T')
            text_widget = tk.Text(self.app.root, **options)
            text_widget.pack()
            self.app.widgets[id] = text_widget
            return id

        def toplevel(self, title="Untitled Toplevel", id=None, **options):
            if id is None:
                id = self._generate_id('TL')
            toplevel = tk.Toplevel(self.app.root, **options)
            toplevel.title(title)
            self.app.widgets[id] = toplevel
            return id

        # Note: Treeview is part of the ttk module
        def treeview(self, id=None, **options):
            if id is None:
                id = self._generate_id('TV')
            treeview = ttk.Treeview(self.app.root, **options)
            treeview.pack()
            self.app.widgets[id] = treeview
            return id
