'''import turtle as t
import time
c=t.clone()
t.color("orange")
c.color("red")
t.circle(100)
c.circle(60)
time.sleep(5)'''



'''import turtle as t
import time
t.begin_fill()
for i in range (4):
    t.fd(100)
    t.rt(90)
t.fillcolor("blue")
t.end_fill()
time.sleep(5)'''



import turtle as t
import time
t.begin_fill()
n=10
while n<=40:
    t.circle(n)
    n=n+10
t.fillcolor("red")
t.end_fill()
time.sleep(5)
