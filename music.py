import pygame
import sqlite3


class SoundPlayer:
    def init(self):
        pygame.mixer.init()

    def play_steps(self, sound_file):
        try:
            conn = sqlite3.connect('settings.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM settings")
            result = cursor.fetchone()
            if result is None:
                volume_music = 70
                volume_game = 80
                cursor.execute("INSERT INTO settings (volume_music, volume_game) VALUES (?, ?)",
                               (volume_music, volume_game))
            else:
                volume_music, volume_game = result
            conn.close()
        except Exception:
            volume_music = 70
            volume_game = 80

        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.set_volume(30)
        pygame.mixer.music.play(-1)

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()
