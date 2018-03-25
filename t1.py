import rake
import operator
import sys

text = sys.argv[1]

rake_object = rake.Rake("stopwords_pt.txt", 4, 3, 0)

#sample_file = open("x", 'r')

#text = sample_file.read()

keywords = rake_object.run(text)
print "Keywords:", keywords
print text
kw = []
for name in keywords:
	if  name[1]>1:
		kw.append(name[0])

myList = ','.join(map(str, kw))

print myList
