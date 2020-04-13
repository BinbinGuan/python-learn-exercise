t = open("/Users/guanbinbin/Downloads/workspace/python-learn-exercise/mysql.txt",'w')
try:
    t.write("Hello, ")
    t.write("World!")
finally:
    t.close()
print(t)

with open("/Users/guanbinbin/Downloads/workspace/python-learn-exercise/mysql.txt",'w') as w:
    w.write("Hello, ")
    w.write("World!")



t1 = open("/Users/guanbinbin/Downloads/workspace/python-learn-exercise/mysql.txt",'r')
for i in range(3):
    print(str(i)+":"+t1.readline())


t1 = open("/Users/guanbinbin/Downloads/workspace/python-learn-exercise/mysql.txt",'r')
print(t1.readlines())
# import sys
# text=sys.stdin.read()
# words = text.split()
# wordCount= len(words)
# print("wordcount ",wordCount)

l = list(open("/Users/guanbinbin/Downloads/workspace/python-learn-exercise/mysql.txt", 'r'))
print(l)


m = open("/Users/guanbinbin/Downloads/workspace/python-learn-exercise/day21/test1.txt", 'r')
for line in m.readlines():
    print("***"+line)
m.close()

