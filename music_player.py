import tkinter as tkr
from tkinter.filedialog import askdirectory
import os
import pygame
from tkinter import messagebox

# Initialize the main application window
music_player = tkr.Tk()
music_player.title("My Music Player")
music_player.geometry("450x350")

# Ask the user to select a directory containing music files
directory = askdirectory()
if directory:
    os.chdir(directory)
    # Get only valid audio files
    song_list = [song for song in os.listdir() if song.endswith('.mp3')]
else:
    song_list = []

# Check if songs are available
if not song_list:
    song_list = ["No MP3 files found!"]
    messagebox.showerror("Error", "No MP3 files found in the selected directory!")

# Create playlist
play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg='cyan', selectmode=tkr.SINGLE)
for pos, item in enumerate(song_list):
    play_list.insert(pos, item)

# Initialize pygame mixer
pygame.init()
pygame.mixer.init()

# Define playback control functions
def play():
    if song_list and play_list.curselection():
        try:
            pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
            var.set(play_list.get(tkr.ACTIVE))
            pygame.mixer.music.play()
        except Exception as e:
            messagebox.showerror("Error", f"Unable to play the song. Details: {e}")
    else:
        messagebox.showinfo("Info", "Please select a valid song to play.")

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

# Create buttons and song title label
Button1 = tkr.Button(music_player, width=10, height=2, font="Helvetica 12 bold", text="PLAY", command=play, bg="blue", fg="white")
Button2 = tkr.Button(music_player, width=10, height=2, font="Helvetica 12 bold", text="STOP", command=stop, bg="red", fg="white")
Button3 = tkr.Button(music_player, width=10, height=2, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="purple", fg="white")
Button4 = tkr.Button(music_player, width=10, height=2, font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="orange", fg="white")

var = tkr.StringVar()
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

# Arrange widgets in the window
song_title.pack()
play_list.pack(fill="both", expand="yes")
Button1.pack(side="left", padx=5, pady=5)
Button2.pack(side="left", padx=5, pady=5)
Button3.pack(side="left", padx=5, pady=5)
Button4.pack(side="left", padx=5, pady=5)

# Debugging: Print directory and song list to console
print(f"Selected Directory: {directory}")
print(f"Song List: {song_list}")

# Run the application
music_player.mainloop()

