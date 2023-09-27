import PySimpleGUI as sg
import pytube

layout = [
    [sg.Input(key='video_url', tooltip="Enter URL")],
    [sg.Button('Download')]
]

window = sg.Window('Youtube Video', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Download':
        video_url = values['video_url']

        video_instance = pytube.YouTube(video_url)
        stream = video_instance.streams.get_highest_resolution()
        stream.download()

window.close()
