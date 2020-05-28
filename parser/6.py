(x1, y1) = tuple(input().split())
(x2, y2) = tuple(input().split())
(x0, y0) = tuple(input().split())

(X1, Y1) = tuple(input().split())
(X2, Y2) = tuple(input().split())
(X0, Y0) = tuple(input().split())
x1 = float (x1)
x2 = float (x2)
y1 = float (y1)
y2 = float (y2)
x0 = float (x0)
y0 = float (y0)

X1 = float (X1)
X2 = float (X2)
Y1 = float (Y1)
Y2 = float (Y2)
X0 = float (X0)
Y0 = float (Y0)

k = (y2 - y1) / (x2 - x1)
b = y0 - k * x0

K = (Y2 - Y1) / (X2 - X1)
B = Y0 - K * X0

x = (B - b) / (k - K)
print ("ans:")
print (x)

print (k * x + b)
# a->AB || DB 