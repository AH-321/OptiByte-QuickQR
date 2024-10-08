Function inst_main()
    Set oShell = WScript.CreateObject("WScript.Shell")

    ' Install Python
    oShell.Run "cmd /c winget install python & echo Python installation complete. Cloning source... & pause", 1, true

    ' Clone the repository
    oShell.Run "cmd /c git clone https://github.com/AH-321/OptiByte-QuickQR & pause", 1, true

    ' Create virtual environment
    oShell.Run "cmd /c python -m venv .\.venv & pause", 1, true

    ' Activate virtual environment
    oShell.Run "cmd /c .\venv\Scripts\activate.bat & pause", 1, true

    ' Install requirements
    oShell.Run "cmd /c pip install -r requirements.txt & pause", 1, true

    ' Finished setup
    oShell.Run "cmd /c echo Finished setting up environment. Running QuickQR... & pause", 1, true

    ' Wait a moment before running the next command
    WScript.Sleep 2000
    oShell.Run "cmd /c python QuickQR.py", 1, true
End Function

inst_main()

