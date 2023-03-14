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

    def insert(self, mname):
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
        list = self.driver.find_elements(By.XPATH, '//div[@id="comments"]/div[@class="comment-item "]/div[@class="comment"]')
        time.sleep(3)
        for li in list:
            try:
                dic = {}
                dic['comments'] = li.find_element(By.XPATH, './/p/span[@class="short"]').text
                vgrade = li.find_element(By.XPATH, './/h3/span[2]/span[2]').get_attribute('class')  # //*[@id="hot-comments"]/div[2]/div/h3/span[2]/span[2]
                grade = '无'
                if vgrade == "allstar50 rating":
                    grade = 5
                elif vgrade == "allstar40 rating":
                    grade = 4
                elif vgrade == "allstar30 rating":
                    grade = 3
                elif vgrade == "allstar20 rating":
                    grade = 2
                elif vgrade == "allstar10 rating":
                    grade = 1
                dic['grade'] = grade
                # dic['vgrade'] = vgrade
                self.lst.append(dic)
            except Exception as e:
                print(e)
        # print(self.lst)
        with open(f'{mname}.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['comments', 'grade'])
            writer.writeheader()
            writer.writerows(self.lst)
    # def b1(self):
    #     self.getdata()
    #
    # def b2(self, mname1):
    #     self.insert(mname=mname1)




