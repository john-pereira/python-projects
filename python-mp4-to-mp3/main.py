import moviepy.editor as me
import PySimpleGUI as sg

layout = [
    [sg.Text('Video File'), sg.Input(key='video_file'), sg.FileBrowse()],
    [sg.Text('Output Audio File'), sg.Input(key='audio_file'), sg.FileSaveAs()],
    [sg.Button('Convert')]
]

window = sg.Window('Video to Audio Converter', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Convert':
        video_file = values['video_file']
        audio_file = values['audio_file']

        # Convert video to audio
        video = me.VideoFileClip(video_file)
        audio = video.audio
        audio.write_audiofile(audio_file)

        sg.popup('Conversion successful!', title='Success')

window.close()
