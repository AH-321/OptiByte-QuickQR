# Installation:

Windows:
  1. Simply run ```installer.vbs```

Unix-like systems:
  1. Download and extract .zip file
  2. Move to the extracted folder using ```cd /path/to/extractedfolder```
  3. In the QuickQR directory, create a virtual environment using ```python -m venv .venv/```
  4. Activate the virtual environment using ```.venv/Scripts/activate``` (```activate.fish``` if using FISH)
  5. Install dependencies using ```pip install -r requirements.txt``` (make sure the venv is active)
  6. Run ```python QuickQR.py```

# Please note:
This program does not currently auto detect cameras. You will need to configure them manually in ```decode.py```. The default is ```0```, which is usually the built-in camera. If using and external camera (webcam, DroidCam, etc.) you will need to select the corresponding number for that camera: ```1```, ```2```, etc.
