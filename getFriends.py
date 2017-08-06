# itChat
Use itchat to find many interesting story of WeChat daily
import itchat
itchat.login()
#获取好友信息
#此处会弹出二维码登陆
firends=itchat.get_friends(update=True)[0:]

#初始化
male=female=other=0
#去掉0（自己）
for i in firends[1:]:
    sex=i["Sex"]
    if sex==1:
        male +=1
    elif sex==2:
        female +=1
    else:
        other +=1
#好友总数
total=len(firends[1:])
#输出性别比例
print("男性朋友：  %2f%%" % (float(male)/total*100))
print("女性朋友：  %2f%%" % (float(female)/total*100))
print("不知性别朋友：  %2f%%" % (float(other)/total*100))

#获取各个变量的函数
def get_var(var):
    variable=[]
    for i in firends:
        value=i[var]
        variable.append(value)
    return variable
# 获取变量
NickName=get_var("NickName")
Sex=get_var("Sex")
Province=get_var("Province")
City=get_var("City")
Signature=get_var("Signature")


from pandas import DataFrame
data={
    "NickName":NickName,
    "Sex":Sex,
    "Province":Province,
    "City":City,
    "Signature":Signature
}
frame=DataFrame(data)
frame.to_csv("../DataSaving/data.csv",index=True)

#获取个性签名，制作词云图

import re
siglist=[]
for i in firends:
    signature=i["Signature"].strip().replace("span","").replace("class","").replace("emoji","")
    rep=re.compile("1f\d+\w*|[<>/=]")
    signature=rep.sub("",signature)
    siglist.append(signature)
text="".join(siglist)

# 分词
import jieba
wordlist=jieba.cut(text,cut_all=True)
word_space_split=" ".join(wordlist)

# 画图
import matplotlib.pylab as plt
from wordcloud import WordCloud,ImageColorGenerator
import numpy as np
import PIL.Image as Image

coloring = np.array(Image.open("../Image/test.png"))
my_wordcloud=WordCloud(background_color="white",max_words=2000,
                       mask=coloring,max_font_size=60,random_state=42,scale=2,
                       font_path="../Font/simhei.ttf").generate(word_space_split)

image_colors=ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)

# plt.axes("off")
plt.show()


