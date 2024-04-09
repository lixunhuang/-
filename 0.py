import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
formatted_questions_list = []

def simulate_click(url):
    # 设置 Chrome 为无头模式
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # 使浏览器不显示界面

    # 创建浏览器对象
    driver = webdriver.Chrome(options=chrome_options, executable_path='C:/Users/O/AppData/Local/Google/Chrome/Application/chromedriver.exe')

    # 访问页面
    driver.get(url)
    # 查找包含总页数的元素
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    page_remark = soup.find('p', class_='pageRemark')

    # 从元素中提取总页数
    total_pages = int(page_remark.find('b').text)

    # 模拟鼠标点击事件，如果有具体的元素需要点击，请使用对应的定位方式
    # 这里使用 document.body.click() 模拟在页面的任意位置进行点击
    for j in range(total_pages - 1):
        for i in range(10):
            print(j, i)
            reference_answer_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "参考答案")

            if len(reference_answer_links) > i:
                # 点击第 i 个链接元素
                reference_answer_links[i].click()
            # 等待页面加载，可以根据实际情况调整等待时间
            else:
                break
            driver.implicitly_wait(5)

            try:
                # 尝试执行点击操作
                driver.execute_script(
                    "document.evaluate(\"//*[contains(text(), '查看')][1]\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();")
            except Exception as e:
                # 如果发生异常，输出异常信息，但继续执行下一步
                pass          # # 点击“已有账号，去登陆”
            # login_link = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, "//a[@href='/user.php?act=login']"))
            # )
            # login_link.click()
            # # 等待页面加载
            # 这里可以使用适当的等待方法，确保页面加载完成后再进行下一步操作

            # 输入账号
            # account_input = driver.find_element(By.NAME, "account")  # 假设账号输入框的 name 属性为 "username"
            # account_input.clear()  # 清空输入框
            # account_input.send_keys("1503858173@qq.com")  # 输入账号
            #
            # # 输入密码
            # password_input = driver.find_element(By.NAME, "password")  # 假设密码输入框的 name 属性为 "password"
            # password_input.clear()  # 清空输入框
            # password_input.send_keys("che471130385")  # 输入密码
            #
            # # 提交登录
            # login_button = driver.find_element(By.NAME, "登录")
            # login_button.click()
            try:
                # 获取点击后的页面内容
                page_content = driver.page_source
                soup = BeautifulSoup(page_content, 'html.parser')

                # 提取问题
                question_element = soup.find('div', class_='essaytitle')
                question = question_element.find('h1').text.strip()

                # 提取选项
                options_element = soup.find('div', class_='essaytitle')
                try:
                    options = options_element.find_all('p')[1].text.strip()
                except Exception as e:
                    options = ''
                    pass

                # 提取答案
                answer_element = soup.find('div', class_='listbg')
                answer = answer_element.text.strip().replace("参考答案：", "")
                # 关闭浏览器
                # 整合成指定格式的字符串
                formatted_question = f"{question}\n{options}\n答案是{answer}.\n<EOF>"

                # 存储到列表
                formatted_questions_list.append(formatted_question)
            except Exception as e:
                # 如果发生异常，输出异常信息，但继续执行下一步
                driver.back()
                continue          # # 点击“已有账号，去登陆”
            if i == 0 and j == 0:
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "电工复审题库"))
                )
                # Click on the element
                element.click()
            else:
                try:
                    driver.back()
                except Exception as e:
                    print(j, i)

        try:
            next_page_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "下一页"))
            )
            next_page_element.click()
        except Exception as e:
            file_path = "电工复审题库.txt"
            # 打开文件，使用写入模式（'w'）
            with open(file_path, 'w', encoding='utf-8') as file:
                # 将列表中的每个字符串写入文件
                for question in formatted_questions_list:
                    file.write(question + '\n')
            print(j ,i)
        # Click on the "下一页" element
    file_path = "电工复审题库.txt"

    # 打开文件，使用写入模式（'w'）
    with open(file_path, 'w', encoding='utf-8') as file:
        # 将列表中的每个字符串写入文件
        for question in formatted_questions_list:
            file.write(question + '\n')
    driver.quit()

    return page_content

url = "https://www.asklib.com/t18593/t18595.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

# 使用 headers 模拟浏览器访问，防止被识别为爬虫
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # 使用Beautiful Soup解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 在这里添加根据网页结构提取信息的代码
    # 请查看Beautiful Soup文档以了解更多信息 https://www.crummy.com/software/BeautifulSoup/bs4/doc/

    # 示例：提取所有标题
    titles = soup.find_all('h2')
    for title in titles:
        print(title.text)

    # 添加模拟鼠标点击事件
    clicked_page_content = simulate_click(url)

    # 使用 BeautifulSoup 解析点击后的页面内容
    clicked_soup = BeautifulSoup(clicked_page_content, 'html.parser')

    # 在这里添加根据点击后的页面结构提取信息的代码
    # 示例：提取点击后页面的标题
    clicked_titles = clicked_soup.find_all('h2')
    for title in clicked_titles:
        print(f"Clicked Page Title: {title.text}")

else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
