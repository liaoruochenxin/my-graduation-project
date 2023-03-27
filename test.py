from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Spider:
    lst = []
    def __init__(self):
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option('detach', True)  # 不自动关闭浏览器
        self.driver = webdriver.Chrome()

    def getdata(self):
        self.driver.get('https://movie.douban.com/')
        time.sleep(2)

    def insert(self):
        mname = input()
        self.driver.find_element(By.ID, 'inp-query').send_keys(mname)
        time.sleep(1)
        self.driver.find_element(By.ID, 'inp-query').send_keys(Keys.ENTER)  # 回车
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//div[@class="title"]/a').click()
        time.sleep(2)
        self.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight)'  # 0表示x轴滚动距离，后面的表示y轴滚动到底
        )
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//div[@id="comments-section"]/div[1]/h2/span/a').click()  # //*[@id="comments-section"]/div[1]/h2/span/a
        time.sleep(2)
        for i in range(1, 11):
            time.sleep(1)
            self.driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)'  # 0表示x轴滚动距离，后面的表示y轴滚动到底
            )
            # 等待指定元素出现
            WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='comment']")))

            list = self.driver.find_elements(By.XPATH, '//div[@id="comments"]/div[@class="comment-item "]/div[@class="comment"]')
            for li in list:
                try:
                    dic = {}
                    dic["comment"] = li.find_element(By.XPATH, './/p/span[@class="short"]').text
                    dic["area"] = li.find_element(By.XPATH, './/h3/span[@class="comment-info"]/span[@class="comment-location"]').text
                    dic["time"] = li.find_element(By.XPATH, './/h3/span[@class="comment-info"]/span[@class="comment-time "]').text
                    dic["grade"] = li.find_element(By.XPATH, './/h3/span[2]/span[2]').get_attribute("class")
                    if dic["grade"] == "allstar50 rating":
                        dic["grade"] = '5'  # 换成字符格式，因为如果用整型会警告
                    elif dic["grade"] == "allstar40 rating":
                        dic["grade"] = '4'
                    elif dic["grade"] == "allstar30 rating":
                        dic["grade"] = '3'
                    elif dic["grade"] == "allstar20 rating":
                        dic["grade"] = '2'
                    elif dic["grade"] == "allstar10 rating":
                        dic["grade"] = '1'
                    else:
                        dic["grade"] = "未给出分数"
                    self.lst.append(dic)
                except Exception as e:
                    print(e)
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//div[@id="paginator"]/a[3]').click()
        # print(self.lst)
        with open(f'{mname}.csv', 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['comment', 'grade', 'time', 'area'])
            writer.writeheader()
            writer.writerows(self.lst)


spider = Spider()
spider.getdata()
spider.insert()



