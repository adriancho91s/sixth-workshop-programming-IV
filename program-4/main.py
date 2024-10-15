import io
import os
import gradio as gr
from PIL import Image
import pygame
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from mutagen.flac import FLAC


class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.cover_image = None

    def load_icon(self, filename):
        script_dir = os.path.dirname(__file__)
        return os.path.join(script_dir, filename)

    def play_music(self, song):
        if song:
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            if song.endswith('.mp3'):
                self.show_cover(song)
            elif song.endswith('.flac'):
                self.show_flac_cover(song)
            return f"Now playing: {os.path.basename(song)}"
        else:
            return "Please select a music file"

    def pause_music(self):
        pygame.mixer.music.pause()
        return "Music paused"

    def resume_music(self):
        pygame.mixer.music.unpause()
        return "Music resumed"

    def stop_music(self):
        pygame.mixer.music.stop()
        self.cover_image = None
        return "Music stopped"

    def show_cover(self, song):
        audio = MP3(song, ID3=ID3)
        for tag in audio.tags.values():
            if tag.FrameID == 'APIC':
                cover_data = tag.data
                cover_image = Image.open(io.BytesIO(cover_data))
                cover_image = cover_image.resize((200, 200), Image.LANCZOS)
                self.cover_image = cover_image
                break
        del audio

    def show_flac_cover(self, song):
        audio = FLAC(song)
        if audio.pictures:
            cover_data = audio.pictures[0].data
            cover_image = Image.open(io.BytesIO(cover_data))
            cover_image = cover_image.resize((200, 200), Image.LANCZOS)
            self.cover_image = cover_image
        del audio

    def get_cover_image(self):
        if self.cover_image:
            return self.cover_image
        else:
            return None


player = MusicPlayer()

css = """
        #play_button, #pause_button, #resume_button, #stop_button {
            background-color: #1DB954;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
            width: 50px;
            height: 50px;
            background-size: cover;
        }
        
        #play_button {
          display: inline-block;
          width: 3em;
          height: 3em;
          --svg: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23000' fill-opacity='0' stroke='%23000' stroke-dasharray='40' stroke-dashoffset='40' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M8 6l10 6l-10 6Z'%3E%3Canimate fill='freeze' attributeName='fill-opacity' begin='0.5s' dur='0.15s' values='0;0.3'/%3E%3Canimate fill='freeze' attributeName='stroke-dashoffset' dur='0.5s' values='40;0'/%3E%3C/path%3E%3C/svg%3E");
          background-color: currentColor;
          -webkit-mask-image: var(--svg);
          mask-image: var(--svg);
          -webkit-mask-repeat: no-repeat;
          mask-repeat: no-repeat;
          -webkit-mask-size: 100% 100%;
          mask-size: 100% 100%;
        }
        
        #pause_button {
          display: inline-block;
          width: 3em;
          height: 3em;
          --svg: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cg fill='none' stroke='%23000' stroke-dasharray='32' stroke-dashoffset='32' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M7 6h2v12h-2Z'%3E%3Canimate fill='freeze' attributeName='stroke-dashoffset' dur='0.4s' values='32;0'/%3E%3C/path%3E%3Cpath d='M15 6h2v12h-2Z'%3E%3Canimate fill='freeze' attributeName='stroke-dashoffset' begin='0.4s' dur='0.4s' values='32;0'/%3E%3C/path%3E%3C/g%3E%3C/svg%3E");
          background-color: currentColor;
          -webkit-mask-image: var(--svg);
          mask-image: var(--svg);
          -webkit-mask-repeat: no-repeat;
          mask-repeat: no-repeat;
          -webkit-mask-size: 100% 100%;
          mask-size: 100% 100%;
        }
        
        #resume_button {
          display: inline-block;
          width: 3em;
          height: 3em;
          --svg: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 2048 2048'%3E%3Cpath fill='%23000' d='M384 256h128v1536H384zm1472 768L768 1792V256zm-960 521l738-521l-738-521z'/%3E%3C/svg%3E");
          background-color: currentColor;
          -webkit-mask-image: var(--svg);
          mask-image: var(--svg);
          -webkit-mask-repeat: no-repeat;
          mask-repeat: no-repeat;
          -webkit-mask-size: 100% 100%;
          mask-size: 100% 100%;
        }
        
        #stop_button {
          display: inline-block;
          width: 3em;
          height: 3em;
          --svg: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23000' d='M2 12c0-4.714 0-7.071 1.464-8.536C4.93 2 7.286 2 12 2s7.071 0 8.535 1.464C22 4.93 22 7.286 22 12s0 7.071-1.465 8.535C19.072 22 16.714 22 12 22s-7.071 0-8.536-1.465C2 19.072 2 16.714 2 12'/%3E%3C/svg%3E");
          background-color: currentColor;
          -webkit-mask-image: var(--svg);
          mask-image: var(--svg);
          -webkit-mask-repeat: no-repeat;
          mask-repeat: no-repeat;
          -webkit-mask-size: 100% 100%;
          mask-size: 100% 100%;
        }
        
        #play_button:hover, #pause_button:hover, #resume_button:hover, #stop_button:hover {
            background-color: #1ed760;
        }
        .gradio-container .gr-file, .gradio-container .gr-textbox {
            border: 2px solid #1DB954;
            border-radius: 12px;
            padding: 10px;
            font-size: 16px;
        }
    """

with gr.Blocks(css=css) as demo:
    gr.Markdown("# Music Player Interface")

    with gr.Row():
        song_input = gr.File(label="Select a music file", file_types=[".mp3", ".flac", '.wav', '.mp4'])

    cover_output = gr.Image(label="Cover Image")

    with gr.Row():
        play_button = gr.Button("Play", elem_id="play_button")
        pause_button = gr.Button("Pause", elem_id="pause_button")
        resume_button = gr.Button("Resume", elem_id="resume_button")
        stop_button = gr.Button("Stop", elem_id="stop_button")

    play_button.click(player.play_music, inputs=song_input, outputs=gr.Textbox())
    pause_button.click(player.pause_music, outputs=gr.Textbox())
    resume_button.click(player.resume_music, outputs=gr.Textbox())
    stop_button.click(player.stop_music, outputs=gr.Textbox())
    song_input.change(player.get_cover_image, outputs=cover_output)

demo.launch()
