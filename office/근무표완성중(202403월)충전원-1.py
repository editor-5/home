
a = {'주간': '이성용', '야간': '이재평', '휴무': '김기석'}
b = {'주간': '무무무', '야간': '이성용', '휴무': '이재평'}
c = {'주간': '이재평', '야간': '김기석', '휴무': '이성용'}
d = {'주간': '     ', '야간': '이재평', '휴무': '이성용'}
e = {'주간': '     ', '야간': '이성용', '휴무': '이재평'}
f = {'주간': '     ', '야간': '     ',  '휴무': '이재평,이성용'}
g = {'주간': '이성용', '야간': '    ',  '휴무': '이재평'}
h = {'주간': '이재평', '야간': '이성용', '휴무': '   '}
i = {'주간': '무무무', '야간': '이재평', '휴무': '이성용'}

data = [a, b, c, d, e, f, g, h, i]

# a ->x c, b ->x a, c ->x b,    
# a ->x h, b ->x g, c ->x i   
# d ->x b, e ->x a, f ->x c  
# d ->x i, e ->x g, f ->x h
# g ->x i, g ->x b
# h->x g, h->x a
# i ->x h, i ->x c

for _ in range(15):

  print(data[data.index(e)])   
  print(data[data.index(d)]) 
for _ in range(1):
  
  print(data[data.index(e)])
   
  

