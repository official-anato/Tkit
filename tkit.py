import tkinter as tk
from tkinter import ttk
from collections import defaultdict

class App:
    def __init__(self, title="Untitled Window", x=130, y=130, default_pack_method='pack'):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{x}x{y}")
        self.widgets = {}
        self.widget_counters = defaultdict(int)
        self.default_pack_method = default_pack_method
        self.create = self.Create(self)

    def getwidlist(self):
        return self.widgets

    def getwid(self, id):
        return self.widgets.get(id)

    def run(self):
        self.root.mainloop()

    def set_widget_value(self, id, value):
        widget = self.widgets.get(id)
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)
            widget.insert(0, value)
        elif isinstance(widget, tk.Text):
            widget.delete('1.0', tk.END)
            widget.insert('1.0', value)
        elif isinstance(widget, ttk.Progressbar):
            widget['value'] = value
        elif isinstance(widget, tk.Scale):
            widget.set(value)
        elif isinstance(widget, tk.Spinbox):
            widget.delete(0, tk.END)
            widget.insert(0, value)
        elif isinstance(widget, tk.Listbox):
            widget.selection_clear(0, tk.END)
            widget.selection_set(value)
        elif isinstance(widget, tk.Checkbutton) or isinstance(widget, tk.Radiobutton):
            var = self.widgets.get(f"{id}_var")
            var.set(value)
        else:
            raise ValueError(f"Unsupported widget type: {type(widget)}")

    def get_widget_value(self, id):
        widget = self.widgets.get(id)
        if isinstance(widget, tk.Entry) or isinstance(widget, tk.Text) or isinstance(widget, tk.Spinbox):
            return widget.get()
        elif isinstance(widget, ttk.Progressbar):
            return widget['value']
        elif isinstance(widget, tk.Scale):
            return widget.get()
        elif isinstance(widget, tk.Listbox):
            selection = widget.curselection()
            if selection:
                return selection[0]
            else:
                return None
        elif isinstance(widget, tk.Checkbutton) or isinstance(widget, tk.Radiobutton):
            var = self.widgets.get(f"{id}_var")
            return var.get()
        else:
            raise ValueError(f"Unsupported widget type: {type(widget)}")

    class Create:
        def __init__(self, app):
            self.app = app

        def _generate_id(self, prefix):
            self.app.widget_counters[prefix] += 1
            return f"{prefix}{self.app.widget_counters[prefix]}"

        def _pack_widget(self, widget, pack_method, **pack_options):
            if pack_method == 'pack':
                widget.pack(**pack_options)
            elif pack_method == 'grid':
                widget.grid(**pack_options)
            elif pack_method == 'place':
                widget.place(**pack_options)
            else:
                raise ValueError(f"Invalid pack method: {pack_method}")

        def label(self, text="Untitled Label", id=None, pack_method=None, **options):
            if id is None:
                id = self._generate_id('L')
            label = tk.Label(self.app.root, text=text, **options)
            pack_method = pack_method or self.app.default_pack_method
            self._pack_widget(label, pack_method, **options.get('pack_options', {}))
            self.app.widgets[id] = label
            return id

        def button(self, text="Untitled Button", id=None, pack_method=None, **options):
            if id is None:
                id = self._generate_id('B')
            button = tk.Button(self.app.root, text=text, **options)
            pack_method = pack_method or self.app.default_pack_method
            self._pack_widget(button, pack_method, **options.get('pack_options', {}))
            self.app.widgets[id] = button
            return id

        def entry(self, id=None, pack_method=None, **options):
            if id is None:
                id = self._generate_id('E')
            entry = tk.Entry(self.app.root, **options)
            pack_method = pack_method or self.app.default_pack_method
            self._pack_widget(entry, pack_method, **options.get('pack_options', {}))
            self.app.widgets[id] = entry
            return id

        def dropdown(self, selected_choice="", options=[], id=None, pack_method=None, **other):
            if id is None:
                id = self._generate_id('D')
            selected_choice = tk.StringVar(self.app.root)
            selected_choice.set(selected_choice)
            dropdown = tk.OptionMenu(self.app.root, selected_choice, *options, **other)
            pack_method = pack_method or self.app.default_pack_method
            self._pack_widget(dropdown, pack_method, **other.get('pack_options', {}))
            self.app.widgets[id] = dropdown
            return id

        def checkbox(self, text="", id=None, pack_method=None, **options):
            if id is None:
                id = self._generate_id('C')
            var = tk.BooleanVar(self.app.root)
            checkbox = tk.Checkbutton(self.app.root, text=text, variable=var, **options)
            pack_method = pack_method or self.app.default_pack_method
            self._pack_widget(checkbox, pack_method, **options.get('pack_options', {}))
            self.app.widgets[id] = checkbox
            self.app.widgets[f"{id}_var"] = var
            return id

        def message(self, text="Untitled Message", id=None, pack_method=None, **options):
            if id is None:
                id = self._generate_id('MSG')
            message = tk.Message(self.app.root, text=text, **options)
            pack_method = pack_method or self.app.default_pack_method
            self._pack_widget(message, pack_method, **options.get('pack_options', {}))
            self.app.widgets[id] = message
            return id

        def text(self, id=None, pack_method=None, **options):
            if id is None:
                id = self._generate_id('T')
            text_widget = tk.Text(self.app.root, **options)
            pack_method = pack_method or self.app.default_pack_method
            self._pack_widget(text_widget, pack_method, **options.get('pack_options', {}))
            self.app.widgets[id] = text_widget
            return id

        def radio_button(self, text="", value=None, variable=None, id=None, command=None, pack_method=None, **options):
            if id is None:
                id = self._generate_id('R')
            if variable is None:
                variable = tk.StringVar(self.app.root)
            radio_button = tk.Radiobutton(self.app.root, text=text, value=value, variable=variable, command=command, **options)
            pack_method = pack_method or self.app.default_pack_method
            self._pack_widget(radio_button, pack_method, **options.get('pack_options', {}))
            self.app.widgets[id] = radio_button
            self.app.widgets[f"{id}_var"] = variable
            return id

        def scale(self, from_=0, to=100, orient=tk.HORIZONTAL, id=None, command=None, pack_method=None, **options):
            if id is None:
                id = self._generate_id('S')
            scale = tk.Scale(self.app.root, from_=from_, to=to, orient=orient, command=command, **options)
            pack_method = pack_method or self.app.default_pack_method
            self._pack_widget(scale, pack_method, **options.get('pack_options', {}))
            self.app.widgets[id] = scale
            return id

        def listbox(self, id=None, command=None, pack_method=None, **options):
            if id is None:
                id = self._generate_id('LB')
            listbox = tk.Listbox(self.app.root, **options)
            if command is not None:
                listbox.bind('<<ListboxSelect>>', command)
            pack_method = pack_method or self.app.default_pack_method
            self._pack_widget(listbox, pack_method, **options.get('pack_options', {}))
            self.app.widgets[id] = listbox
            return id

        def spinbox(self, from_=0, to=100, id=None, command=None, pack_method=None, **options):
            if id is None:
                id = self._generate_id('SB')
            spinbox = tk.Spinbox(self.app.root, from_=from_, to=to, command=command, **options)
            pack_method = pack_method or self.app.default_pack_method
            self._pack_widget(spinbox, pack_method, **options.get('pack_options', {}))
            self.app.widgets[id] = spinbox
            return id

        def progressbar(self, mode='determinate', id=None, pack_method=None, **options):
            if id is None:
                id = self._generate_id('PB')
            progressbar = ttk.Progressbar(self.app.root, mode=mode, **options)
            pack_method = pack_method or self.app.default_pack_method
            self._pack_widget(progressbar, pack_method, **options.get('pack_options', {}))
            self.app.widgets[id] = progressbar
            return id

        def notebook(self, id=None, pack_method=None, **options):
            if id is None:
                id = self._generate_id('NB')
            notebook = ttk.Notebook(self.app.root, **options)
            pack_method = pack_method or self.app.default_pack_method
            self._pack_widget(notebook, pack_method, **options.get('pack_options', {}))
            self.app.widgets[id] = notebook
            return id

        def treeview(self, columns=None, id=None, pack_method=None, **options):
            if id is None:
                id = self._generate_id('TV')
            treeview = ttk.Treeview(self.app.root, columns=columns, **options)
            pack_method = pack_method or self.app.default_pack_method
            self._pack_widget(treeview, pack_method, **options.get('pack_options', {}))
            self.app.widgets[id] = treeview
            return id

        def separator(self, parent_menu_id, id=None, **options):
            if id is None:
                id = self._generate_id('SEP')
            parent_menu = self.app.widgets.get(parent_menu_id)
            if parent_menu is None:
                raise ValueError(f"Parent menu with id '{parent_menu_id}' not found.")
            separator = parent_menu.add_separator(**options)
            self.app.widgets[id] = separator
            return id

        def menu_item(self, parent_menu_id, label=None, command=None, id=None, **options):
            if id is None:
                id = self._generate_id('MI')
            parent_menu = self.app.widgets.get(parent_menu_id)
            if parent_menu is None:
                raise ValueError(f"Parent menu with id '{parent_menu_id}' not found.")
            menu_item = parent_menu.add_command(label=label, command=command, **options)
            self.app.widgets[id] = menu_item
            return id

        def submenu(self, parent_menu_id, label=None, id=None, **options):
            if id is None:
                id = self._generate_id('SM')
            parent_menu = self.app.widgets.get(parent_menu_id)
            if parent_menu is None:
                raise ValueError(f"Parent menu with id '{parent_menu_id}' not found.")
            submenu = tk.Menu(parent_menu, **options)
            parent_menu.add_cascade(label=label, menu=submenu)
            self.app.widgets[id] = submenu
            return id

        def menu(self, id=None, **options):
            if id is None:
                id = self._generate_id('M')
            menu = tk.Menu(self.app.root, **options)
            self.app.root.config(menu=menu)
            self.app.widgets[id] = menu
            return id

        def frame(self, id=None, pack_method=None, **options):
            if id is None:
                id = self._generate_id('F')
            frame = tk.Frame(self.app.root, **options)
            pack_method = pack_method or self.app.default_pack_method
            self._pack_widget(frame, pack_method, **options.get('pack_options', {}))
            self.app.widgets[id] = frame
            return id

        def canvas(self, id=None, pack_method=None, **options):
            if id is None:
                id = self._generate_id('C')
            canvas = tk.Canvas(self.app.root, **options)
            pack_method = pack_method or self.app.default_pack_method
            self._pack_widget(canvas, pack_method, **options.get('pack_options', {}))
            self.app.widgets[id] = canvas
            return id
