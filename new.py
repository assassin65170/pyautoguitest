import pyautogui

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)

#pyautogui.doubleClick(47, 362)
'''
pyautogui.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry"s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', interval=0.1)

pyautogui.alert('Automated')'''


distance = 200

while distance > 0:
        pyautogui.drag(distance, 0, duration=0.5)   
        distance -= 5
        pyautogui.drag(0, distance, duration=0.5)   
        pyautogui.drag(-distance, 0, duration=0.5)  
        distance -= 5
        pyautogui.drag(0, -distance, duration=0.5)  