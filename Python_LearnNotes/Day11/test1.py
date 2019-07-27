'''
selenium实战之模拟事件处理
1.自动化测试实战之ActionChains模拟用户行为
    简介：讲解使用selenium里面的ActionChains模拟用户行为
    需求：需要模拟鼠标操作才能进行的情况，比如单击、双击、点击鼠标右键、拖拽
    解决：selenium提供了一个类来处理这类事件
              selenium.webdriver.common.action_chains.ActionChains(driver)
        脚本：from selenium.webdriver.common.action_chains import ActionChains

    执行原理：调用ActionChains的方法时不会立即执行，会将所有操作按顺序存放在一个列队里，当调用perform()方法时，队列中的事件会依次执行。
        支持链式写法或者分步写法
        ActionChains(driver).click(ele).perform()
        鼠标和键盘方法列表：
                perform()   执行链中的所有动作
                click(on_element=None)      单继鼠标左键
                context_click(on_element=None)    点击鼠标右键
                double_click(on_element=None)     双击鼠标左键
                move_to_element(to_element)       鼠标移动到某个元素
                ele.send_keys(keys_to_send)       发送某个词到当前焦点的元素
                ====不常用====
                click_and_hold(on_element=None)   点击鼠标左键，不松开
                release(on_element=None)          在某个元素位置松开鼠标左键
                key_down(value,element=None)      按下某个键盘上的键
                key_up(value,element=None)        松开某个键
                drag_and_drop(source, target)     拖拽到某个元素然后松开
                drag_and_drop_by_offset(source,xoffset,yoffset)    拖拽到某个坐标然后松开
                move_by_offset(xoffset, yoffset)  鼠标从当前位置移动到某个坐标
                move_to_element_with_offset(to_element, xoffset, yoffset)   移动到距某个元素（左上角坐标）多少距离的位置
                send_keys_to_element(element, keys_to_send)发送某个键到指定元素


2.鼠标事件实战之hover菜单栏弹出
    简介：鼠标事件之菜单栏hover弹出
    #引入AcitionChains类
    from selenium.webdriver.common.action_chains import ActionChains
    move_to_element(to_element)     鼠标移动到某个元素
    # 对定位到的元素执行鼠标移动到上面的操作
    ActionChains（driver）.move_to_element(ele1).perform()


3.多知识点综合实战之模拟用户登录
    简介：讲解使用selenium模拟登录小D课堂，并选择课程
3.1 查找登录框：
login_ele = driver.find_element_by_css_selector("#login")
ActionChains（driver）.click(login_ele).perform()

# 输入用户名
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[1]/input').click()
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[1]/input').clear
driver.find_element_by_xpath(('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[1]/input').send_keys("")
# 输入密码
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[2]/input').click()
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[2]/input').clear
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[2]/input').send_keys("")
# 点击登录    '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[3]/button'
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[3]/button').click()


4.自动化测试实战之网页等待事件
简介：简介自动化测试的等待时间
4.1 为什么需要等待时间——》等系统稳定
网页需要加载对应的资源文件，页面渲染，窗口处理等等
4.2 自动化测试常用的等待事件
4.2.1 强制等待：（自己调试代码看效果）
from time import sleep
sleep（5） #强制等待5秒再执行下一步，缺点是不管资源是不是完成，都必须等待
4.2.2 隐形等待：
driver.implicitly_wait(10)   #隐形等待，最长等10秒
设置了一个最长等待事件，如果在规定时间内网页加载完成，则执行下一步，否则一直等到时间截止，然后执
行下一步；
弊端就是程序会一直等待整个网页加载完成，到浏览器标签栏那个加载圈不再转
注意：对driver起作用，所以只要设置一次即可，没有必要到处设置
4.2.3 显性等待：
WebdriverWait 需要配合until（）和until_not（）方法，可以根据判断条件而进行灵活地等待了，主要的意
思就是：程序每隔N秒检查一次，如果成功，则执行下一步，否则继续等待,直到超过设置的最长时间,然后抛
出TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
语法：WebDriverWait(driver,timeout)
try：
    ele = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.id,"kw")))
    ele.send_keys("小D课堂")
    print（"资源加载成功"）
    print（driver.title）
except：
    print（"资源加载失败，发送报警邮件或短信"）
finally：
    print（"不管是否成功，都打印用于资源清理"）
    #退出浏览器
    river.quit()
结论：隐形和显性可以同时使用，等待的最长时间取两者之中的较大者

'''
