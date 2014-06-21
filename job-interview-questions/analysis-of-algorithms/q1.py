# Contains duplicate output, doesn't handle duplicate values
def threeSumWithHashTable(lst):
  hashMap = {}

  for a in lst:
    # Create a hash map where the key is an item in
    # lst and the value is the number of occurences
    hashMap.clear()
    for l in lst:
      if hashMap.get(l) == None:
        hashMap[l] = 1
      else:
        hashMap[l] += 1

    for b in lst:
      c = -(a + b)

      if a != b and b != c and hashMap.get(c) > 0:
        print a, b, c
        hashMap[c] -= 1

def threeSumWithSorting(lst):
  lst.sort()
  n = len(lst)

  for i in range(0, n-2):
    a = lst[i]
    j = i + 1
    k = n - 1

    while (j < k):
      b = lst[j]
      c = lst[k]

      if (a+b+c > 0):
        k -= 1
      elif (a+b+c < 0):
        j += 1
      else:
        j += 1
        k -= 1

        print a, b, c


if __name__ == '__main__':
  numbers = [3, -1, -4, 2, 1, 5, -2, 0, -3, 4, -5]

  print '3Sum with Hash Table'
  threeSumWithHashTable(numbers)

  print '3Sum with Sorting'
  threeSumWithSorting(numbers)