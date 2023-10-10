from wordcloud import WordCloud
import matplotlib.pyplot as plt

# read the word from a txt file
with open('words.txt', 'r') as f:
    text = f.read()

wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
