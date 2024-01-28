import time
text = 'Example text\nThis is how you would write text for the script to type in the terminal/console\nThis script can be modified and used to create cool terminal applications in python\nenjoy...\n\n >>> BOTnen'
typingspeed = 0.08      #higher is slower

for e in text:
    time.sleep(typingspeed)
    print(e, end="", flush=True)
    