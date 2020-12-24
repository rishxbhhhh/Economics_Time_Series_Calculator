print("SOLN:_________________________________________________________________________________________")
sum_error_xsq = tcal = sum_error_ysq = Sb = Se = expvar = totalvar = sumx = sumy = sumxsq = sumysq = sumxy = meany  = meanx = Rsq = 0.0
sumydiffmean = sumxdiffmean = 0.0
# input values
x = [1,2,3,4]
y = [5450,5860,6270,6680]
# predicted y
yp = []
# y-meany
sumymeany = 0.0
ydiffmean = []
ydiffmeansq = []
# yp-meany
sumypmeany = 0.0
ypdiffmean = []
ypdiffmeansq = []


for i in x:
    sumx = sumx + i
    sumxsq = sumxsq + i*i
meanx = sumx / len(x)

for i in y:
    sumy = sumy + i
    sumysq = sumysq + i*i
    
meany = sumy / len(y)

for i in range(len(x)):
    sumxy = sumxy + x[i]*y[i]
    
a = (sumxsq*sumy - sumx*sumxy) / (len(x)*sumxsq -sumx*sumx)
b = (len(x)*sumxy - sumx*sumy) / (len(x)*sumxsq -sumx*sumx)
# first run the program with accurate value
# round off the value of b upto two decimal places
# a = -8.109
# b = 0.88
meany = round(meany, 2)
for i in range(len(x)):
    t = a + b*x[i]
    yp.append(t)
for i in range(len((x))):
    expvar = expvar + (yp[i] - meany)*(yp[i] - meany)
    totalvar = totalvar + (y[i] - meany)*(y[i] - meany)
Rsq = expvar/totalvar

for i in range(len(x)):
    u = y[i] - meany
    ydiffmean.append(u)
    ydiffmeansq.append(u*u)
    v = yp[i] - meany
    ypdiffmean.append(v)
    ypdiffmeansq.append(v*v)

print("a = %.3f" % round(a, 3))
print("b = %.3f" % round(b, 3))
print("Mean of y = %.3f" % round(meany, 3))
print("Mean of x = %.3f" % round(meanx, 3))
print("___________________________________________________________________________________________\n")
print("  t                 A                   A(t)                 A*t                   t^2\n")
print("___________________________________________________________________________________________\n")
for i in range(len(x)):
    print("%.3f      |      %.3f      |      %.3f      |      %.3f      |      %.3f\n" %( x[i], y[i], yp[i], y[i]*x[i], x[i]*x[i] ))


print("\nsum of t = "+str(round(sumx, 3))+"\nsum of t^2 = "+str(sumxsq)+"\nsum of A = "+str(sumy)+"\nsum of A^2 = "+str(sumysq)+"\nsum of t*A= "+str(sumxy))
print(str(sumy)+" = "+str(len(x))+"a + "+str(sumx)+"b")#eqn1
print(str(sumxy)+" = "+str(sumx)+"a + "+str(sumxsq)+"b")#eqn2