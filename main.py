import gspread
import webbrowser as web
import time
import pyautogui as pg
import numpy as np
import cv2


alph = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_col_num(text , col_name):
    num = 1
    found = 0
    for i in col_name:
        if i == text:
            found = 1
            break
        else:
            num+= 1
    if found:
        return num
    else:
        return 'not found'




def send_messege(
    phone_no: str,
    wait_time: int = 15,
) -> None:
    messge = """Greetings!%0A%0AI'm *RANDOM* , -a candidate for the position of *Hostel Affairs General Secretary* in the upcoming SAC elections. """
    web.open(f"https://web.whatsapp.com/send?phone=+91{phone_no}&text={messge}")
    print(f"messege sent to {phone_no}")
    
    time.sleep(10)
    pg.press("enter")
    time.sleep(1.5)
    pg.hotkey('ctrl', 'w')
    time.sleep(0.5)
    messge = """Greetings!%0A%0AI'm *RANDOM* , -Second messege """
    web.open(f"https://web.whatsapp.com/send?phone=+91{phone_no}&text={messge}")
    print(f"messege sent to {phone_no}")
    
    time.sleep(10)
    pg.press("enter")


    time.sleep(1)
    pg.hotkey('ctrl' , 'v')
    time.sleep(2)
    pg.typewrite("Scan the QR code for the manifesto")
    pg.press('enter')
    time.sleep(3)
    image = pg.screenshot()
    

    image = cv2.cvtColor(np.array(image),
                        cv2.COLOR_RGB2BGR)
    
    # writing it to the disk using opencv
    cv2.imwrite(f"data/{phone_no}.png", image)
    time.sleep(0.5)
    pg.hotkey('ctrl', 'w')
    time.sleep(0.5)




if '__name__' ==  '__main__':
    gs = gspread.service_account(filename= 'token.json')
    worksheet = gs.open('BTECH CONTACT NUMS').sheet1

    #taking inputs
    all_value = worksheet.get_all_values()


    messge = """
    Greetings!

    I'm RANDOM , third year electrical UG, a candidate for the position of Hostel Affairs General Secretary in the upcoming SAC elections. 
    """

    messge = """Greetings!%0A%0AI'm *RANDOM* , -a candidate for the position of *Hostel Affairs General Secretary* in the upcoming SAC elections. """

    # #getting column name
    col_name = all_value[0]
    print(col_name)



    #getting column number of is posted 

    posted_col_num = get_col_num('send'  , col_name)

    # #iterating through all the responces and checking if already posted or not
    k=1
    for i in range(1 ,len(all_value) ):
        # print('lats se' , k , ' ' , len(all_value[i]))
        # print(all_value[i][posted_col_num-1])
        k+=1
        if all_value[i][posted_col_num-1] == '':
            number = all_value[i][0]

            send_messege( number )

            cell = alph[posted_col_num]+str(i+1)
            print(cell)
            worksheet.update(cell , 1)    

            print("do something")
            # print(all_value[i][posted_col_num-1])

