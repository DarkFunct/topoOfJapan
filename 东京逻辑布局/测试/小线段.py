from Tokyo_logistic_topo.kml_tool import ITDKkml
point1={'longitude':136.9025,'latitude':35.1598}
point2={'longitude':127.675,'latitude':26.185}
section=5
lo_section=(point1['longitude']-point2['longitude'])/section
la_section=(point1['latitude']-point2['latitude'])/section
print(lo_section,la_section)
tem1={}
tem2={}
tem1['longitude']=point1['longitude']
tem1['latitude']=point1['latitude']
tem2['longitude']=point1['longitude']-lo_section
tem2['latitude']=point1['latitude']-la_section

filename_KML = './file/1234.kml'
f=open(filename_KML,'w')
paint = ITDKkml(f)
paint.head()
i=1
while i<5:
    print(tem1,tem2)
    paint.draw_edge(start=tem1,end=tem2)
    i+=1
    tem1['longitude']=tem2['longitude']
    tem1['latitude']=tem2['latitude']
    tem2['longitude']=point1['longitude']-lo_section*i
    tem2['latitude']=point1['latitude']-la_section*i
paint.draw_edge(start=tem1,end=point2)
paint.tail()
f.close()