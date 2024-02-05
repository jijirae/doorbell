from flask import Flask, render_template, request
import pygame

app = Flask(__name__)

# Initialize pygame
pygame.mixer.init()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alert', methods=['POST'])
def alert():
    # Code to handle the alert
    pygame.mixer.music.load('doorbell_sound.mp3')  # replace 'alert_sound.wav' with the path or name to your sound file
    pygame.mixer.music.play()
    return 'Alert triggered successfully'

if __name__ == '__main__':
    # Change '0.0.0.0' to your actual IP address (local)
    # Run ipconfig on a terminal to check your IP.
    app.run(host='0.0.0.0', port=5000, debug=True)
