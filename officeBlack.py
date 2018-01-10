from _winreg import *

keyVal = r'Software\Microsoft\Office\16.0\Common'
key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
themeVal = QueryValueEx(key, "UI Theme")[0]
print 'Registry start', themeVal

if themeVal != 4:
    try:
        SetValueEx(key, "UI Theme", 0, REG_DWORD, 4)
    except:
        pass
CloseKey(key)

key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_READ)
themeVal = QueryValueEx(key, "UI Theme")[0]
print 'Registry value finish', themeVal
CloseKey(key)
