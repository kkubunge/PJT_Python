
import pyautogui
import time
import win32api
import keyboard
import random
import datetime
import os

keyDown_List = ['enter',' ',' ',' ',' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
# timeOut = [0.1, 0.3, 0.5, 1, 10]
timeOut = [0.1, 0.3]
random_Enter = 0
shutdownHour_Parm = 2;
shutdownMin_Parm = 51;

startTime = datetime.datetime.now()
targetTime = startTime + datetime.timedelta(hours=shutdownHour_Parm, minutes=shutdownMin_Parm)

startTime_Str = "Start Time : "
startTime_Str += startTime.strftime("%Y")
startTime_Str += "-"
startTime_Str += startTime.strftime("%m")
startTime_Str += "-"
startTime_Str += startTime.strftime("%d")
startTime_Str += " "
startTime_Str += startTime.strftime("%H")
startTime_Str += ":"
startTime_Str += startTime.strftime("%M")
startTime_Str += ":"
startTime_Str += startTime.strftime("%S")
startTime_Str += "\n"

targetTime_Str = "End Time : "
targetTime_Str += targetTime.strftime("%Y")
targetTime_Str += "-"
targetTime_Str += targetTime.strftime("%m")
targetTime_Str += "-"
targetTime_Str += targetTime.strftime("%d")
targetTime_Str += " "
targetTime_Str += targetTime.strftime("%H")
targetTime_Str += ":"
targetTime_Str += targetTime.strftime("%M")
targetTime_Str += ":"
targetTime_Str += targetTime.strftime("%S")
targetTime_Str += "\n"

pyautogui.move(1300, 150)
pyautogui.click()

pyautogui.write(startTime_Str)
pyautogui.write(targetTime_Str)


while True:

    random_Enter = 0
    now = datetime.datetime.now()

    if now > targetTime :
        print("Time End Bye~~")
        pyautogui.write("\nTime End Bye~~\n")

        now_Str = "Real End Time : "
        now_Str += now.strftime("%Y")
        now_Str += "-"
        now_Str += now.strftime("%m")
        now_Str += "-"
        now_Str += now.strftime("%d")
        now_Str += " "
        now_Str += now.strftime("%H")
        now_Str += ":"
        now_Str += now.strftime("%M")
        now_Str += ":"
        now_Str += now.strftime("%S")
        now_Str += "\n"
        pyautogui.write(now_Str)
        os.system("shutdown /s /t 1")
        break


    if keyboard.is_pressed('esc') :
        print("break gogo")
        break

    keyVal = random.choice(keyDown_List)

    pyautogui.keyDown(keyVal)
    # print("keyDown ", keyVal)
    # pyautogui.press(keyVal)
    # print("press ", keyVal)
    pyautogui.keyUp(keyVal)
    # print("keyUp ", keyVal)

    random_Enter = random.randrange(1,10)

    if random_Enter < 2 :
        pyautogui.press(keyDown_List[0])

    sleepTime = random.choice(timeOut) * random.randrange(1,10)
    print(sleepTime)
    time.sleep(sleepTime)







# while True:

# 키다운 이벤트 받기
    # down = win32api.GetKeyState(0x01)
    # if down == 0:
# 키다운 이벤트가 esc
    # if keyboard.is_pressed('esc'):
    #     print("????")
    #     break

    # # 좌표출력
    # print(pyautogui.position())

    # pyautogui.press(random.choice(keyDown_List))

    # sleepTime = random.choice(timeOut) * random.randrange(1,10)
    # time.sleep(sleepTime)


    # print("2222")
    # # time.sleep(0.1)
    # sleepTime = random.choice(timeOut) * random.randrange(1,10)
    # time.sleep(sleepTime)





# # # https://blog.naver.com/heavencoding/223091727830
# timeOut = [0.1, 0.3, 0.5, 1, 10]
# sleepTime = random.choice(timeOut) * random.randrange(1,10)
# print("sleepTime = ", sleepTime)
# sleepTime = random.choice(timeOut) * random.randrange(1,10)
# print("sleepTime = ", sleepTime)
# sleepTime = random.choice(timeOut) * random.randrange(1,10)
# print("sleepTime = ", sleepTime)
# sleepTime = random.choice(timeOut) * random.randrange(1,10)
# print("sleepTime = ", sleepTime)
# sleepTime = random.choice(timeOut) * random.randrange(1,10)
# print("sleepTime = ", sleepTime)
# sleepTime = random.choice(timeOut) * random.randrange(1,10)
# print("sleepTime = ", sleepTime)
# sleepTime = random.choice(timeOut) * random.randrange(1,10)
# print("sleepTime = ", sleepTime)
# sleepTime = random.choice(timeOut) * random.randrange(1,10)
# print("sleepTime = ", sleepTime)
# sleepTime = random.choice(timeOut) * random.randrange(1,10)
# print("sleepTime = ", sleepTime)
# sleepTime = random.choice(timeOut) * random.randrange(1,10)
# print("sleepTime = ", sleepTime)
# sleepTime = random.choice(timeOut) * random.randrange(1,10)
# print("sleepTime = ", sleepTime)



# import os

# os.system("shutdown /s /t 1")
# # /s 옵션 : PC를 종료
# # /t 1 옵션 : 종료 전 1초 딜레이를 설정


# import datetime

# Now = datetime.datetime.now()
# print("지금 날짜 + 시간 : ", Now)

# # 1시간 : 1시간 전/후
# print("\ntimedelta ", datetime.timedelta(hours=1))
# print("한 시간 전 : ", Now - datetime.timedelta(hours=1))
# print("한 시간 후 : ", Now + datetime.timedelta(hours=1))

# # 하루 : 내일/어제
# print("\ntimedelta ", datetime.timedelta(days=1))
# print("내일 : ", Now  + datetime.timedelta(days=1))
# print("어제 : ", Now - datetime.timedelta(days=1))

# # 30분 : 30분 전/후
# print("\nimedelta ", datetime.timedelta(minutes=30))
# print("30분 전 : ", Now - datetime.timedelta(minutes=30))
# print("30분 후 : ", Now + datetime.timedelta(minutes=30))

# print("\n0.5시간 후 : ", Now + datetime.timedelta(hours=0.5))





# import pyautogui
# import time
# # 원하는 그림을 화면에서 찾아서... 클릭하기
# p_list = pyautogui.locateAllOnScreen("E:\80_Program\Python\Python_TEST\Input_Img\source.png")
# p_list = list(p_list)
# print(p_list)

# p_center = pyautogui.center(p_list[0])
# pyautogui.click(p_center)




# while True:

# # 키다운 이벤트 받기
#     # down = win32api.GetKeyState(0x01)
#     # if down == 0:
# # 키다운 이벤트가 enter면
#     if keyboard.is_pressed('enter'):
#         print("????")
#         break

#     print("11111")
#     # 좌표출력
#     print(pyautogui.position())

#     print("2222")
#     time.sleep(0.1)


# # sleep
# time.sleep(0.1)

# # pyautogui 모듈을 가져옵니다.
# import pyautogui
# # 마우스를 현재 위치에서 X 방향으로 200, Y 방향으로 200 이동합니다.
# pyautogui.move(200, 200)


# # 마우스를 현재 위치에서 X 방향으로 200, Y 방향으로 200 이동합니다.
# # 마지막 인자인 듀레이션 3을 넣으면 좌표로 3초동안 이동합니다.
# pyautogui.move(200, 200, 3)

# # position 함수는 마우스의 현재 위치를 반환합니다.
# x, y = pyautogui.position()

# # 마우스 클릭
# pyautogui.click()
# # 마우스 우클릭
# pyautogui.click(button='right')
# x=39, y=23 3초간 이동해서 마우스 우클릭
# pyautogui.click(x=39, y=23, duration=3, button='right')

# # 300, 100 좌표 클릭
# pyautogui.click(300, 100)
# # 한글자에 0.3초 간 Hello~ NGMsoftware! 입력
# pyautogui.write("\nHello~ NGMsoftware!", interval=0.3)

# # hotkey ctrl+a
# pyautogui.hotkey("ctrl", "a")
# # hotkey ctrl+c
# pyautogui.hotkey("ctrl", "c")
# # hotkey ctrl+v
# pyautogui.hotkey("ctrl", "v"))

# # keyDown, press, keyUp을 사용하면 실제 눌러진것처럼 보인다.
# pyautogui.keyDown("shift")
# # presses=10 은 10번 누르기
# pyautogui.press("a", presses=10)
# pyautogui.keyUp("shift")
# pyautogui.press('enter', presses=3, interval=3)

# ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
# ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
# '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '', ']', '^', '_', '`',
# 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
# 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
# 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
# 'browserback', 'browserfavorites', 'browserforward', 'browserhome',
# 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
# 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
# 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
# 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
# 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
# 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
# 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
# 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
# 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
# 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
# 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
# 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
# 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
# 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
# 'command', 'option', 'optionleft', 'optionright']


# # 메모장 실행
# import os
# os.system('notepad.exe')
