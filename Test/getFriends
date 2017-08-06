# itChat
# Use itchat to find many interesting story of WeChat daily
import itchat
itchat.login()

#Get friends information
#Before landing this will pop up two-dimensional code
firends=itchat.get_friends(update=True)[0:]

#Initialization
male=female=other=0

#Removing ourselves
for i in firends[1:]:
    sex=i["Sex"]
    if sex==1:
        male +=1
    elif sex==2:
        female +=1
    else:
        other +=1
#Total of  our friends
total=len(firends[1:])

#Print sex accounting
print("Male：  %2f%%" % (float(male)/total*100))
print("Female：  %2f%%" % (float(female)/total*100))
print("Other：  %2f%%" % (float(other)/total*100))

#Defining a function to achieve every variable
def get_var(var):
    variable=[]
    for i in firends:
        value=i[var]
        variable.append(value)
    return variable
#Achieve every variable
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

#Get personalized signature and making word clouds

import re
siglist=[]
for i in firends:
    signature=i["Signature"].strip().replace("span","").replace("class","").replace("emoji","")
    rep=re.compile("1f\d+\w*|[<>/=]")
    signature=rep.sub("",signature)
    siglist.append(signature)
text="".join(siglist)

# Cut every word
import jieba
wordlist=jieba.cut(text,cut_all=True)
word_space_split=" ".join(wordlist)

#Making word clouds
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


