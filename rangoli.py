# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
def print_rangoli(n):

   small = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e',
                    6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14:
         'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}


  
   list1 = []
   if n==1:
      print('a')
   else:

   
    for j in reversed(range(0, n+1)):

       str1 = ''.join(list1)

       str2 = str1[::-1]
       str3 = str2[3:]

       if str1 != '':
        print(str1.rjust(2*n, '-'), end='')
        print(str3.ljust(n+(n-3), '-'))

       list1.clear()

       for i in reversed(range(j, n+1)):
        if i != 0:

            list1.append(small[i])
            list1.append('-')

   list2 = []

   for k in (range(0, n+1)):

    str01 = ''.join(list2)

    str02 = str01[::-1]
    str03 = str02[3:]

    if str01 != '':
        print(str01.rjust(2*n, '-'), end='')
        print(str03.ljust(n+(n-3), '-'))

    list2.clear()

    for l in reversed(range(k+2, n+1)):
        if l != 0:

            list2.append(small[l])
            list2.append('-')



n = int(input())
print_rangoli(n)