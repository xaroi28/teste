# Bibliotecas
import os
import pyautogui
from time import sleep
import subprocess
from PIL import Image

# 1 - Abrir dominio sistemas
response = os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Domínio Contábil\domínio folha.lNK")
print(response)
pyautogui.sleep(5)
pyautogui.hotkey('SHIFT', 'TAB')
for i in range(10):
    pyautogui.press('delete')
pyautogui.write("GERENTE")
pyautogui.press('TAB')
pyautogui.press('DELETE')
pyautogui.write("GERENTE")
pyautogui.press('TAB')
pyautogui.press('TAB')
pyautogui.press('ENTER')
pyautogui.press('RIGHT')
pyautogui.press('ENTER')
