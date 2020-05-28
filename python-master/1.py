n = len (objects)
cnt = 0
for i in range (n):
  a = True
  for j in range (i + 1, n):
    if objects[i] is objects[j]:
      a = False
  if a == True:
    cnt+=1
print (cnt)
