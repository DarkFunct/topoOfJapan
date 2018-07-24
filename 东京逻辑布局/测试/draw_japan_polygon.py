#-*- coding:utf-8 -*-

'''
point in polygon问题，因为是大致范围，所以不要求精确性，不考虑点在多边形边上的复杂情况
@tar_point:目标点，为一个字典{'longitude';num_l,'latitude':num_2}
@polygon:目标多边形，为一个列表，[point_1,point_2,...,point_n]
'''
def point_in_polygon(tar_point,polygon):
    flag = False
    i=0
    size = len(polygon)
    while i<size:
        start = i%size
        end = (i+1)%size
        if tar_point['latitude'] < (min(polygon[start]['latitude'],polygon[end]['latitude']))or \
                tar_point['latitude'] > (max(polygon[start]['latitude'],polygon[end]['latitude'])) or \
                polygon[start]['latitude'] == polygon[end]['latitude']:
            i = i+1
        else:
            res_longi = (tar_point['latitude']-polygon[start]['latitude'])*\
                        (polygon[end]['longitude']-polygon[start]['longitude'])/\
                        (polygon[end]['latitude']-polygon[start]['latitude'])+polygon[start]['longitude']
            if res_longi>tar_point['longitude']:
                flag = not flag
            i = i+1
    return flag
point = {'longitude': 1, 'latitude': 0.2}
po = [{'longitude': 0, 'latitude': 0},{'longitude': 1, 'latitude': 1},{'longitude': 2, 'latitude': 0}]
print(point_in_polygon(point,po))