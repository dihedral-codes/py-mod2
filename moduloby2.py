twos = lambda n, t: [[i*2**j % 12 for i in range(n)] for j in range(t)]

transpose = lambda d, n: [-i % n for i in d]

def power(d, i, n):
  if i < 1:
    return None
  result = d
  while i > 1:
   result = onlyodd([((j + k) % n) for j in d for k in result])
   i -= 1
  return result

def onlyodd(l):
  result = []
  for i in set(l):
    if l.count(i) % 2 == 1:
      result.append(i)
  return result

def bytwo(n):
  prevs = []
  next = list(range(n))
  while next not in prevs:
    prevs.append(next)
    next = [(i * 2) % n for i in next]
  return prevs

def latex_bytwo(n):
  rows = bytwo(n)

  print("\\begin{tabular}{" + ("r" * len(rows)) + "}")
  print("\\toprule")
  for i in range(n):
    s = ""
    for x in rows:
      s = s + "$" + str(x[i]) + "$" + " & "
    print(s[:len(s)-2] + '\\\\')
  print("\\bottomrule")
  print("\\end{tabular}")

