#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 19:03:31 2024

@author: hatemdumlu
"""

"""
Created on Tue Jun 25 18:41:01 2024

@author: user
"""
import h5py
import pandas as pd
import os
import json






# Excel dosyasının adı ve yolu
excel_file = '/home/hatemdumlu/h5/dosya_target_etiket.xlsx'


# Ana görüntülerin olduğu dosya yolu
ana_goruntuler_yolu = '/home/hatemdumlu/h5/data'


# Excel dosyasını pandas DataFrame olarak oku
df = pd.read_excel(excel_file)

# Her bir dosya için label bilgisini ekleyelim
for index, row in df.iterrows():
    dosya_adi = row['Dosya Adı']
    label = row['Label']
    
    # H5 dosyasının yolu
    h5_path = os.path.join(ana_goruntuler_yolu, dosya_adi)
    
    # Label bilgisini H5 dosyasına object olarak ekleyelim
    label_info = {
        'label': label,
        'description': 'Tumor segmentation label',
        'color': 'red'
    }
    
    with h5py.File(h5_path, 'r+') as h5_file:
        # JSON formatına çevirerek object olarak ekleyelim
        json_data = json.dumps(label_info)
        h5_file.create_dataset('label', data=json_data.encode('utf-8'), dtype=h5py.special_dtype(vlen=str))

print("Label bilgisi H5 dosyalarına object olarak başarıyla eklendi.")