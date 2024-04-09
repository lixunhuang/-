from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 使用 ChromeDriverManager 自动获取并安装 ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://cart.taobao.com/cart.htm?spm=a2141.241046-cn.1997525049.1.70cb5adb2RSsG7&from=mini&pm_id=1501036000a02c5c3739")
time.sleep(10)

search_input_xpath = '//*[@id="J_Item_5442119299837"]/ul/li[1]/div/div/div/label'
search_input = driver.find_element(By.XPATH, search_input_xpath)
search_input.click()
# //*[@id="J_Item_5441553702793"]/ul/li[1]/div/div/div/label
# //*[@id="J_Item_5441553702793"]/ul/li[1]/div/div/div/label
# 定位搜索按钮并点击
search_button_xpath = '//*[@id="J_Order_s_572059930_1"]/div[1]/div/div/label'
search_button = driver.find_element(By.XPATH, search_button_xpath)
search_button.click()
# 获取首页标题

search_button_xpath0 = '//*[@id="J_Go"]'
search_button0 = driver.find_element(By.XPATH, search_button_xpath0)
search_button0.click()

title = driver.title
print(f"淘宝首页标题：{title}")
# 访问网页等其他操作...

search_button_xpath1 = '//*[@id="submitOrderPC_1"]/div[1]/a[2]'
search_button1 = driver.find_element(By.XPATH, search_button_xpath1)
search_button1.click()

# 关闭浏览器窗口
driver.quit()
