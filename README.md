# asteroids

## build instructions

prerequisites:
- python 3.10 or similar, idk what else it might be compatible with
- pip - we gotta install some requirements like pygame
- venv - python virtual environment, a place to host our game away from everything else

----

clone the repo
    - put it wherever you want but we gotta clone first

make sure you got your prerequisites taken care of

navigate to the repo in a terminal, i'm using ubuntu wsl, so if you're using something else, instructions may vary, they should still be similar though

run this command
```bash
python3 -m venv venv
```

activate the virtual environment
```bash
source venv/bin/activate
```

you should see (venv) at the beginning of your terminal prompt, mine looks like
```bash
(venv) krallsm@DESKTOP~/repositories/asteroids$
```

you cloned the repo right?

run this command to install the requirements, they're in the repo
```bash
pip install -r requirements.txt
```

make sure pygame is installed
```bash
python3 -m pygame
```

if you plan to stay in the terminal and aren't using a code editor or anything, you can go ahead and just run it
```bash
python3 main.py
```

if you're in a code editor or something, just restart the code editor and you should be able to use your fancy tools. In VS Code, it'll even open the venv for you :)

enjoy

i'm not really versioning or anything yet, this is still an early work in progress, updates will be random and without warning and just cause