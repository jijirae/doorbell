# 🔔 doorbell-py
A doorbell that runs on your local network through Flask. Requires Python.

## ✅ Requirements
Python: https://www.python.org/downloads/

pygame: ```pip install pygame```

Flask: ```pip install Flask```

## ⚙ Installation
1. Download/clone the repo
2. Run ```run.bat```
3. Profit!

## 👨‍🏫 Usage
* To access the webpage, enter the url in any browser. The url should be your local IP address with Port 5000. (EX: http://192.168.10.5:5000)
* To change the sound, download a .wav/.mp3 file and replace the `Doorbell_sound.mp3`. The name should be the same.
* I highly recommend printing your IP address as a URL QR Code and paste it on your door. (Which is the original intent behind this project)
* You can also use Task Scheduler to open the program once you open your PC.
* You can change the name of the user on the webpage. 

## 🙋‍♂️ How it works
The program uses Flask to run a server which serves the webpage on your network. The webpage features a button which when clicked, sends a POST request to ```doorbell.py``` which uses the ```pygame``` library to play a sound in the directory.

## 🧯 TODO
- [ ] Add a way to terminate the program (Currently, you can terminate it using Task Manager>Details>pythonw.exe)

- [ ] Design the page better (Halfmoon CSS is a good choice!)

- [ ] Make it easier to change the user's name on the webpage

Made with 💖 by Raeji
