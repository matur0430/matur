import  wikipedia
a=input("검색하고 싶은것을 검색해보세요!(단,영어일것) : ")
wiki=wikipedia.page(a)
text=wiki.content
print(text)

from wordcloud import WordCloud
wd=WordCloud(width =2000, height = 1500).generate(text)
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(wd)
plt.show()
#20307 김해람