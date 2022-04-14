from astropy import units as u
import numpy as np
import matplotlib.pyplot as plt

file = open('/home/mschochet/AST4930/HW7/sed.txt', 'r')
data = np.loadtxt(file, delimiter=',')

x = data [:, 0]
y = data [:, 1]
new_x =[]
new_y = []
greater_ten = np.where(x >= 10.0)
less_thousand = np.where(x <= 1000.0)
for i in range (len(greater_ten[0])):
    new_x.append(x[i])
    new_y.append(y[i])
                
final_x = np.asarray(new_x)
final_y = np.asarray(new_y)

total_integrate = np.trapz(new_x, new_y, 1.0)
ergspersecond = (total_integrate * u.erg) /( u.second)
solLum = ergspersecond.to(u.solLum)

fig, yx1 = plt.subplots(1, 1)
fig.set_size_inches(6, 4)
yx1.plot(np.asarray(x), np.asarray(y))
yx1.set_xscale('log')
yx1.set_yscale('log')
yx1.set_xlabel('specific luminosity')
yx1.set_xlabel('microns')

fig.savefig('schochet_meir_hw7.png')
print(ergspersecond)
print(solLum)
