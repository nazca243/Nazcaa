import time
import sys

def animate_text(text: str, delay: float = 0.1) -> None:
    """Prints out a given text character by character with a delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyric(lyric: str, delay: float, speed: float) -> None:
    """Sings a given lyric with a delay and speed."""
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song() -> None:
    """Sings a song with multiple lyrics."""
    lyrics = [
        ("I just wanna be yours", 0.13),   
        ("Secrets I have held in my heart", 0.13),
        ("Are harder to hide than I thought", 0.11),
        ("Maybe I just wanna be yours", 0.13),
        ("I wanna be yours, I wanna be yours", 0.11) ,
        ("Wanna be yoursssssssssss", 0.13),
        ("Wanna be yoursssssssssssss", 0.11),
        ("Wanna be yourssssssssssss", 0.11),
    ]
    delays = [0.20, 1.0, 0.20, 0.20, 0.30, 0.20, 0.20, 0.20]
    for i in range(len(lyrics)  ):
        lyric, speed = lyrics[i]
        sing_lyric(lyric, delays[i], speed)

if __name__ == "__main__":
    sing_song()