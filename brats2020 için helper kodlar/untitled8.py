import h5py

# H5 dosyasının yolu
h5_path = '/home/hatemdumlu/h5/data/volume_256_slice_1.h5'

# H5 dosyasını oku
with h5py.File(h5_path, 'r') as h5_file:
    for key in h5_file.keys():
        dataset = h5_file[key]
        if isinstance(dataset, h5py.Dataset):
            if dataset.shape == ():  # Skaler veri olup olmadığını kontrol et
                print(f"Skaler veri - {key}: {dataset[()]}")

    # Ayrıca, dosyanın attributelarını da kontrol edelim
    for attr in h5_file.attrs:
        print(f"Attribute - {attr}: {h5_file.attrs[attr]}")