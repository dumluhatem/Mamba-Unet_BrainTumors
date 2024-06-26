import h5py
import pandas as pd
import os

# Ana görüntülerin olduğu dosya yolu
ana_goruntuler_yolu = '/home/hatemdumlu/h5/data'

# Excel dosyasının yolu ve adı
excel_file = '/home/hatemdumlu/h5/dosya_target_etiket.xlsx'

# Excel dosyasını pandas DataFrame olarak oku
df = pd.read_excel(excel_file)

# Her bir dosya için label bilgisini ekleyelim
for index, row in df.iterrows():
    dosya_adi = row['Dosya Adı']
    label = row['Label']
    
    # H5 dosyasının yolu
    h5_path = os.path.join(ana_goruntuler_yolu, dosya_adi)
    
    # H5 dosyasına label bilgisini skaler veri olarak ekleyelim
    with h5py.File(h5_path, 'r+') as h5_file:
        if 'data' in h5_file:
            del h5_file['data']
        h5_file.create_dataset('data', data=label)

print("Label bilgisi h5 dosyalarına skaler veri olarak 'data' adıyla başarıyla eklendi.")