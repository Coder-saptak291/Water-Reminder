import time
from plyer import notification
name = input("Enter your name=")
while True:
    notification.notify(
        title = f"{name} please drink water now",
        message = """Water helps your body:
Keep a normal temperature. Lubricate and cushion joints. Protect your spinal cord and other sensitive tissues. Get rid of wastes through urination, perspiration, and bowel movements.06-Jun-2022
""",
        # app_icon = "D:\My_Python_Experiments\Short projects\icon1.jpg",
        timeout = 15,
        
    )
    time.sleep(60*15)
    