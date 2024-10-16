# Looping
a = 1
b = 2
c = 5

while a < c:
    a = a + 1
    b = b + c
#endwhile
print(f"a = {a}, b = {b}, c = {c}")

d = 4
e = 6
f = 7

while d > f:
    d += 1
    e -= 1

print(f"d = {d}, e = {e}, f = {f}")

g = 4
h = 6

while g < h:
    g = g + 1

print(f" g = {g}, h = {h}")
 
 #Fourth test
j = 2
k = 5
n = 9 

while j < k:
    m = 6
    while m < n:
        print("Goodbye")
        m += 1
    j += 1

#Fifth test
j = 2
k = 5
m = 6
n = 9

while j < k:
    while m < n:
        print("Hello")
        m = m + 1
    #endwhile
    j = j + 1
#endwhile

#Sixth test
p = 2
q = 4

while p < q:
    print("Adios")
    r = 1
    while r < q:
        print("Adios")
        r += 1
    p += 1
