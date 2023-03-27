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
            WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='comment']")))  # 等待指定元素出现
            comments = self.driver.find_elements(By.XPATH, '//div[@id="comments"]/div[@class="comment-item "]/div[@class="comment"]/p/span[@class="short"]')
            gelements = self.driver.find_elements(By.XPATH, '//div[@id="comments"]/div[@class="comment-item "]/div[@class="comment"]/h3/span[@class="comment-info"]/span[2]')
            dates = self.driver.find_elements(By.XPATH, '//div[@id="comments"]/div[@class="comment-item "]/div[@class="comment"]/h3/span[@class="comment-info"]/span[3]')
            areas = self.driver.find_elements(By.XPATH, '//div[@id="comments"]/div[@class="comment-item "]/div[@class="comment"]/h3/span[@class="comment-info"]/span[4]')
            time.sleep(1)
            for date in dates:
                dic = {}
                dic["times"] = date.text
                self.lst.append(dic)
            for area in areas:
                dic = {}
                dic["areas"] = area.text
                self.lst.append(dic)
            for comment in comments:
                dic = {}
                dic["comments"] = comment.text
                self.lst.append(dic)
            for gelement in gelements:
                dic = {}
                dic["grades"] = gelement.get_attribute("class")
                if dic["grades"] == "allstar50 rating":
                    dic["grades"] = 5
                elif dic["grades"] == "allstar40 rating":
                    dic["grades"] = 4
                elif dic["grades"] == "allstar30 rating":
                    dic["grades"] = 3
                elif dic["grades"] == "allstar20 rating":
                    dic["grades"] = 2
                elif dic["grades"] == "allstar10 rating":
                    dic["grades"] = 1
                self.lst.append(dic)
            self.driver.find_element(By.XPATH, '//div[@id="paginator"]/a[3]').click()
        print(self.lst)
        # with open(f'{mname}.csv', 'w', encoding='utf-8', newline='') as f:
        #     writer = csv.DictWriter(f, fieldnames=['comments', 'grades', 'times', 'areas'])
        #     writer.writeheader()
        #     writer.writerows(self.lst)
        with open(f'千寻小姐.csv', 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['comments', 'grades', 'times', 'areas'])
            writer.writeheader()
            writer.writerows(self.lst)

spider = Spider()
spider.getdata()
spider.insert()
