import PySimpleGUI as sg

#make it dark mode you are not a monster also set variables here
sg.theme('dark amber')
val = 90

#setting up the layout
layout = [
    [sg.Button('Drop'), sg.Button('Lift')],
    [sg.Slider(range = (0,180), default_value = val, size = (30,10), orientation = 'h', enable_events = True)]
]

#create the window
window = sg.Window('Window Title', layout)

#main event
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
window.close()