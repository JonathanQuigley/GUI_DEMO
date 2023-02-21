import PySimpleGUI as psgui


def main():
    print("Gui demo")

    layout = [
        [psgui.Text('This is some text in this window')],
        [psgui.Button('PRESS ME')],
        [psgui.Text('Enter some text here', size=(20, 1)), psgui.Input(key='text input')]
    ]

    main_window = psgui.Window(title='This is a window', layout=layout, margins=(125, 125))

    #event loop
    while True:
        event, values = main_window.read()
        if event == psgui.WIN_CLOSED:
            break

    main_window.close()


if __name__ == '__main__':
    main()