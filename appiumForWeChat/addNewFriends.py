from appium import webdriver
import unittest
import time
from appiumForWeChat import *

try:
    desired_caps = driver().drivers()
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    print('创建完成')
    time.sleep(5)
    print("计时完成1")
    driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc='当前所在页面,与的聊天']/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout").click()
    print("进入通讯录页面")
    time.sleep(2)
    print("计时结束2")
    driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc='当前所在页面,与的聊天']/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.mm.ui.mogic.WxViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout").click()
    print("进入新的朋友页面")
    # i=0
    # for i in range(5):
    #     newFriend = driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc='当前所在页面,新的朋友']/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout/android.widget.RelativeLayout["+str(i)+"]")
    #     try:
    #         newFriend.find_element_by_id("com.tencent.mm:id/bmf").click()
    #     except:
    #         print("添加新好友时，出现了问题")
    #     i += 1
    #     print(i)

    newFriend = driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc='当前所在页面,新的朋友']/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout/android.widget.RelativeLayout")
    time.sleep(1)
    try:
        newFriend.find_element_by_id("com.tencent.mm:id/bmf").click()
        time.sleep(1)
        driver.find_element_by_id("com.tencent.mm:id/j0").click()
        time.sleep(1)
        driver.find_element_by_id("com.tencent.mm:id/jc").click()
    except Exception as error:
        print("添加新好友时，出现了问题:" + error)

except Exception as error:
    print("driver有异常" + error)



