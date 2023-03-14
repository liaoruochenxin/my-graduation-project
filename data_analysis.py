import jieba
import jieba.analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# jieba.enable_paddle()  # 开启paddle模式


class data_analysis:

    comments = []
    grades = []

    def read(self, dname):  # 读取文件
        with open(f'{dname}.csv', mode='r', encoding="utf-8") as f:
            f.readline()  # 将光标移动到第二行
            for line in f:
                comment, grade = line.strip().split(",")  # 去除多余字符并以逗号分隔并依次赋值
                self.comments.append(comment)
                self.grades.append(grade)
            comment = ""
            for i in range(0, 5):
                comment += data_analysis.comments[i]
            return comment
                # print(comment, grade)
            # return comment, grade

    def wcloud(self, word):
        back_groud = np.array(Image.open("2708793-bca9e8e36aab4473.png"))
        wordc = WordCloud(background_color="white", font_path="SanJiXingKaiJianTi-Cu-2.ttf", mask=back_groud).generate(word)
        plt.imshow(wordc)
        plt.axis("off")
        plt.show()

    def showg(self, grade):
        plt.plot(grade)
        plt.show()

    def fenci(self, comment):
        kword = jieba.analyse.extract_tags(comment, topK=20, withWeight=False, allowPOS=("n", "nw", "ns", "a", "nt", "nr"))  # 提取主题词
        # print(a)
        # print(jieba.analyse.textrank(comment, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v')))
        return kword


# a = data_analysis()
# a.read()
# comment = ""
# for i in range(0, 5):
#     comment += data_analysis.comments[i]
    # grade += data_analysis.grades[i]

# 测试词云
# kword = " ".join(a.fenci(comment=comment))
# a.wcloud(kword)  # 调用词云

# 测试折线图
# a.showg()

