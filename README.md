# Pomodoro-Timer-Logger

### Description
This is a CLI-based Python application in which a user can start a Pomodoro Technique driven work bracket (i.e. using a timer to break down work into intervals, traditionally a 25 minute period) and log completed intervals to chosen text files (the program is intended to be used with a different text file for each day). This is coupled with another CLI-based Python application which reports how many hours and minutes have been completed weekly. 

**Note:** Python 3 needs to be installed for this program to run. Currently only working on macOS.

### timer-app.py
This is the application used to start the timer and log copleted intervals.

To start: ```python timer-app.py```

The user is initially prompted with an input field ```Enter file name:```, which will be the ```.txt``` file they wish to have the timer log their completed 25 minute intervals in. This should be entered the format ```[DD]-[MM].txt```. If the text file already exists, it will append all logs to that file; If the file does not exist, then the file will be created.

The user is then prompted with an input field to type a start command. If the user enters ```start study```, the program will log ```study``` to the selected text file after the 25 minute bracket. If the user enters ```start work```, the program will instead log ```work``` after the 25 minute bracket. Upon starting the timer with the relevant start command, the CLI will log how many minutes are left in 5 minute intervals. Once the timer runs out and the 25 minute period has been completed, the user will be alerted with both an audio queue ("Jobs done!") and a log in the CLI: ```Work Bracket Done!```. The program then loops back and the user is prompted with the input field ```Enter start command:```.

### report.py
This is the application which gives a report of all the text files currently in the root folder (as said earlier the program is intended to be used with a different text file for each day to allow for weekly reporting).

To start: ```python report.py```

The CLI will then print/log the total hours spend studying, working, and total, based on the text files in the root folder in the format:
```
Total time spent studying: [hour(s)]hr [minute(s)]m
Total time spent working: [hour(s)]hr [minute(s)]m
Total time: [hour(s)]hr [minute(s)]m
```

The user is then prompted with an input: ```Move all logs into a new folder? (y/n):```. If the user enters ```y```, a new folder will be created with a name in the form ```[YYYY]-[MM]-[DD]``` and all the files in the root folder will be moved into that folder. If the user enters ```n```, the program will be terminated.
