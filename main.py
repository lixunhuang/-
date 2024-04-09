from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# 设置Chrome Driver路径
chrome_driver_path = r"C:\Program Files\Google\Chrome\Application".replace('\\', '/')

# 创建Chrome WebDriver实例
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# 打开淘宝首页
driver.get("https://world.taobao.com/?scm=20140651.100.hk")

# 等待页面加载完成
time.sleep(2)

# 定位搜索框
search_box = driver.find_element("xpath", "//input[@id='q']")

# 使用ActionChains模拟人类操作
actions = ActionChains(driver)
actions.move_to_element(search_box).click().send_keys("手机").send_keys(Keys.RETURN).perform()

# 等待搜索结果加载完成
time.sleep(2)

# 在这里你可以执行其他自动化操作，比如点击商品链接等

# 关闭浏览器窗口
driver.quit()
