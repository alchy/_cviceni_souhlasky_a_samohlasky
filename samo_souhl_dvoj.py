# -*- coding: utf-8 -*-

samo = list(tuple('aeiouáéíóú')) 
souh = list(tuple('žščřcjďťňhkrdtnmblmpsvz')) + ['ch'] + ['dž']
dvoj = ['au'] + ['ou'] + ['eu']

text = 'aeiouáéíóúaeiouáéíóúžšch'
#text = 'džin je doma, ouou'

samo_list = list(map(lambda cnt: text.count(cnt), samo))
souh_list = list(map(lambda cnt: text.count(cnt), souh))
dvoj_list = list(map(lambda cnt: text.count(cnt), dvoj))

print('samohlasky v textu {}'.format(text))
for samo, samo_cnt in zip(samo, samo_list):
    print(samo, samo_cnt)

print('souhlasky v textu {}'.format(text))    
for souh, souh_cnt in zip(souh, souh_list):
    if souh_cnt:
        print(souh, souh_cnt)

print('dvojhlásky v textu {}'.format(text))    
for dvoj, dvoj_cnt in zip(dvoj, dvoj_list):
    if dvoj_cnt:
        print(dvoj, dvoj_cnt)
