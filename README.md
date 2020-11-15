# remote-typist

FastAPI server to type on a remote computers keyboard (where the server is
running).

The text to be typed is submitted via an HTML Form. The POST request triggered
on the form submit action triggers the typing on the remote computer.

## Necessary setup:

```
git clone https://github.com/arindas/remote-typist.git
cd remote-typist
pip install -r requirements.txt
```

## Usage:

```
cd remote-typist  # goto git clone directory
./start-server.bash

# or, if you want to specify server HOST and PORT

# HOST = 0.0.0.0, PORT = 5050
HOST="0.0.0.0" PORT="5050" ./start-server.bash
```

Now visit `http://${HOST}:${PORT}` to see the form.
