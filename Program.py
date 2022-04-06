from keytotext import pipeline

nlp = pipeline("mrm8488/t5-base-finetuned-common_gen")
keywordone = ['Law','firm','services']
keywordtwo = ['individual','small business','guardianship']
keywordthree = ['Law','excellence','legal']
keywordfour = ['Law','solutions','problems']
keywordfive = ['Law','case','plan']
#nlp(keywordone)
sortedlist=[]
sentenceone=nlp(keywordone)
print(sentenceone)
sortedlist.append(sentenceone)
sentencetwo=nlp(keywordtwo)
print(sentencetwo)
sortedlist.append(sentencetwo)
sentencethree=nlp(keywordthree)
print(sentencethree)
sortedlist.append(sentencethree)
sentencefour=nlp(keywordfour)
print(sentencefour)
sortedlist.append(sentencefour)
sentencefive=nlp(keywordfive)
print(sentencefive)
sortedlist.append(sentencefive)
import pandas as pd
print(sortedlist)
df = pd.DataFrame(sortedlist)
