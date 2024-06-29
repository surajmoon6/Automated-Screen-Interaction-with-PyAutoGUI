import pyautogui
import time
import pyperclip

# Click on a specific location
pyautogui.click(1639, 1412)
time.sleep(1)

# Move to the start point of the drag
pyautogui.moveTo(992, 207)
# Drag to the end point of the drag
pyautogui.dragTo(2208, 1286, duration=1.0, button='left')

# Press 'Ctrl+C' to copy the selected text
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

# Retrieve the copied text from the clipboard
text = pyperclip.paste()

# Print the retrieved text
print(text)

# Open Notepad
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.typewrite('notepad')
pyautogui.press('enter')
time.sleep(1)

# Paste the copied text into Notepad
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# Save the file
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.typewrite('copied_text.txt')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')  # Confirm the save if prompted
