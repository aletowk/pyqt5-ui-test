# pyqt5-ui-test
PyQt5 app using pyqt5 designer


## How To

* To Edit the MainUi.ui :
```
designer MainUi.ui
```

* Translate XML .ui file into python class :

In "src/gui/" the file MainUI.py must be used with 'designer' app to add widgets etc. After you must run :
```
pyuic5 MainUI.ui > MainUI.py
```