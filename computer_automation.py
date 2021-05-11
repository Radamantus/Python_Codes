# Automatize qualquer processo ou sistema com python
# Importando bibliotecas
import pyautogui
import time

# pyautogui.position()
# pyautogui.KEYBOARD_KEYS

# Mensagem de alerta ao usuário
pyautogui.confirm("Clique OK para confirmar.")
pyautogui.alert("Entrando em modo remoto. Não utilizar o computador.")
pyautogui.PAUSE = 2.0

# Abrir o google drive no meu computador
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(3)
pyautogui.write("https://drive.google.com/drive/my-drive")
pyautogui.press('enter')

# Entrar na minha área de trabalho
pyautogui.hotkey('winleft', 'd')

# Clicar no arquivo para backup e arrastar ele
pyautogui.moveTo(1311, 164)
pyautogui.mouseDown()
pyautogui.moveTo(696, 496)

# Mudar a tela para o google drive
pyautogui.hotkey('alt', 'tab')
time.sleep(1)

# Largar o arquivo no google drive
pyautogui.mouseUp()

# Esperar 5 segundos
time.sleep(5)

# Mensagem de alerta ao usuário
pyautogui.alert("O modo remoto terminou. Computador liberado para uso.")
