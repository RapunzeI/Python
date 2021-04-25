import time

t = time.localtime(1500000000)

print(time.strftime('%A, %B %d %Y', t))
print(time.strftime('%I:%M %p %Z on %m/%d/%Y', t))
print(time.strftime('I will meet you on %a %B %d at %I:%M %p.', t))
