from tkit import App
import tkinter as tk

def update_progress(value):
    app.set_widget_value('PB1', int(value))

def show_selected_item(event):
    selected_item = app.get_widget_value('LB1')
    app.set_widget_value('T1', f"Selected item: {selected_item}")

def show_spinbox_value():
    spinbox_value = app.get_widget_value('SB1')
    app.set_widget_value('T2', f"Spinbox value: {spinbox_value}")

def show_radio_value():
    radio_value = app.get_widget_value('R1')
    app.set_widget_value('T3', f"Radio value: {radio_value}")

app = App(title="Test App", x=400, y=400)

app.create.label(text="Progress Bar:")
app.create.progressbar(id='PB1', length=200)
app.create.scale(from_=0, to=100, command=update_progress)

app.create.label(text="Listbox:")
app.create.listbox(id='LB1', height=5, command=show_selected_item)
app.getwid('LB1').insert(tk.END, "Item 1", "Item 2", "Item 3", "Item 4", "Item 5")
app.create.text(id='T1', height=2, width=30)

app.create.label(text="Spinbox:")
app.create.spinbox(id='SB1', from_=0, to=100, command=show_spinbox_value)
app.create.text(id='T2', height=2, width=30)

app.create.label(text="Radio Buttons:")
radio_var = tk.StringVar(app.root)
app.create.radio_button(text="Option 1", value="Option 1", variable=radio_var, id='R1', command=show_radio_value)
app.create.radio_button(text="Option 2", value="Option 2", variable=radio_var, command=show_radio_value)
app.create.text(id='T3', height=2, width=30)

app.run()
