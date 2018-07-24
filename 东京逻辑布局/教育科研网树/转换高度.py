#-*- coding: UTF-8 -*-
file = '探测的有官方没有.kml'
f1 = open(file,'r+')
infos = f1.readlines()
f1.seek(0,0)
for line in infos:
    line_new = line.replace('111.301407','111.306444').replace('30.737529','30.723747')
    f1.write(line_new)
f1.close()
print(file)