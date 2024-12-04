# Ulauncher NanoID

Ulauncher Extension for generating NanoID strings.

## Features

Generate NanoID with customizable alphabet and length.
Default NanoID uses a combination of NoLookALikeDigits and NoLookALikeCharacters (upper and lower case).
Single argument: Specify length of the NanoID.
Two arguments: Specify alphabet and length of the NanoID.
Screenshots

## Requirements

* ulauncher
* Python >= 2.7
* nanoid (`pip install nanoid`)

## Preview

![Preview](preview.gif)

## Install

Open Ulauncher preferences window -> Extensions -> Add Extension and paste the following URL:

[ulauncher-nanoid](https://github.com/lukas-kd/ulauncher-nanoid)

## Development

```shell
git clone https://github.com/lukas-kd/ulauncher-nanoid
cd ulauncher-nanoid
python -m venv .venv
pip install -r requirements.txt
ln -s ./ ~/.local/share/ulauncher/extensions/ulauncher-nanoid
```

To start debugging the extension, run the following debugging scripts in separate terminal tabs:

```shell
# Terminal 1: Run Ulauncher in development mode
ulauncher --no-extensions --dev -v

# Terminal 2: Run your extension (Update PYTHONPATH and USERNAME to match your local setup)
VERBOSE=1 ULAUNCHER_WS_API=ws://127.0.0.1:5054/ulauncher-nanoid PYTHONPATH=/usr/lib/python3/dist-packages /usr/bin/python3 /home/USERNAME/.local/share/ulauncher/extensions/ulauncher-nanoid/main.py
```

When you make any changes to [main.py](main.py) or other assets, re-run the debugging scripts above.

## License

MIT
