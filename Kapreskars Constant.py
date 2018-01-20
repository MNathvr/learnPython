def ascnum(num):
  return int(''.join(sorted(list(str(num)))))
  
def dscnum(num):
  return int(''.join(sorted(list(str(num)), reverse = True)))
  
def kfunc(innum):
  tries = 0
  res = 0
  while res != 6174:
    tries += 1
    a = ascnum(innum)
    b = dscnum(innum)
    print('a = {0:04d}, b = {1:04d}'.format(a, b))
    if a == b:
      return "This ain't gonna work!"
    if a > b:
      res = a - b 
    else:
      res = b - a 
    if res < 1000:
      res *= 10
    innum = res
  return tries

inputnum = int(input())
print(kfunc(inputnum))
