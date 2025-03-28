import time
import winsound

def play_alarm(sound_file):
    winsound.PlaySound(sound_file, winsound.SND_FILENAME)

def countdown(seconds):
    for remaining in range(seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        timeformat = f'次のアラームまで: {mins:02d}分{secs:02d}秒'
        print(timeformat, end='\r')
        time.sleep(1)
    print(' ' * len(timeformat), end='\r')  # カウントダウン終了後に行をクリア

while True:
    countdown(15 * 60)
    play_alarm('./loop100601.wav')
    countdown(5 * 60)
    play_alarm('./loop100601.wav')
