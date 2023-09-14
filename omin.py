import keyboard
import pyautogui

def on_v_pressed(e):
    pyautogui.moveTo(992,828,0.0001)
    pyautogui.click()
    #예매하기
    pyautogui.moveTo(551,563,0.6)
    pyautogui.click()
    #블록클릭
    pyautogui.moveTo(445,529,0.3)
    pyautogui.click()
    #직접선택
    pyautogui.moveTo(411,545,0.1)
    pyautogui.click()
    pyautogui.moveTo(426,547,0.000001)
    pyautogui.click()
    pyautogui.moveTo(386,532,0.000001)
    pyautogui.click()
    pyautogui.moveTo(397,531,0.000001)
    pyautogui.click()
    #좌석선택
    pyautogui.moveTo(898,813,0.1)
    pyautogui.click()
    #다음단계

keyboard.on_press_key("v", on_v_pressed)

# 프로그램을 계속 실행하도록 유지
keyboard.wait("esc")