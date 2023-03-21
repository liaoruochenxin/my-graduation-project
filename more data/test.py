from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv


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
            comments = self.driver.find_elements(By.XPATH, '//div[@id="comments"]/div[@class="comment-item "]/div[@class="comment"]/p/span[@class="short"]')
            grades = self.driver.find_elements(By.XPATH, '')
            time.sleep(1)
            for comment in comments:
                dic = {}
                dic["comments"] = comment.text
                self.lst.append(dic)
            self.driver.find_element(By.XPATH, '//div[@id="paginator"]/a[3]').click()
        print(self.lst)
        # print(self.lst)
        # with open(f'{mname}.csv', 'w', encoding='utf-8', newline='') as f:
        #     writer = csv.DictWriter(f, fieldnames=['comments', 'grade'])
        #     writer.writeheader()
        #     writer.writerows(self.lst)

spider = Spider()
spider.getdata()
spider.insert()
