# -*- coding:utf-8 -*- 
#  @Time : 2017-11-28 10:52
#  @Author : KhaZix
#  @File : wordcloud_generate.py.py
#  @Description:
#            
#   --Input:
#   --Output:

from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt
f_comment = open("./comments.txt",'rb')
words = []
for line in f_comment.readlines():
    if(len(line))==12:
        continue
    A = jieba.cut(line)
    words.append(" ".join(A))
stopwords = [',','。','【','】', '”','“','，','《','》','！','、','？','.','…','1','2','3','4','5','[',']','（','）',' ']
new_words = []
for sent in words :
    word_in = sent.split(' ')
    new_word_in = []
    for word in word_in:
        if word in stopwords:
            continue
        else:
            new_word_in.append(word)
    new_sent = " ".join(new_word_in)
    new_words.append(new_sent)
final_words = []
for sent in new_words:
    sent = sent.split(' ')
    final_words +=sent
final_words_flt = []
for word in final_words:
    if word == ' ':
        continue
    else:
        final_words_flt.append(word)
text = " ".join(final_words_flt)
font = r'C:\Windows\Fonts\simfang.ttf'
wc = WordCloud(collocations=False, font_path=font, width=1400, height=1400, margin=2).generate(text.lower())
plt.imshow(wc)
plt.axis("off")
plt.show()
wc.to_file('word_cloud.png')  