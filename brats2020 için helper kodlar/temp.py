import h5py
import os

# Birleştirilecek dosyaların bulunduğu dizin
input_directory = "/home/hatemdumlu/h5/slices"  # Verilen dosyanın bulunduğu dizin
output_directory = "/home/hatemdumlu/h5/output11"  # Birleştirilen dosyaların kaydedileceği dizin

os.makedirs(output_directory, exist_ok=True)

# Volume ve slice sayısı
num_volumes = 369
num_slices_per_volume = 155



# Volume ve slice sayısı
num_volumes = 369
num_slices_per_volume = 155

for volume_idx in range(1, num_volumes + 1):
    volume_name = f"volume_{volume_idx}"  # Sıfırlar olmadan
    output_file = os.path.join(output_directory, f"{volume_name}.h5")
    print(f"Volume {volume_idx} yapılıyor .")
    # Birleştirme işlemi için çıktı dosyasını oluşturun
    with h5py.File(output_file, 'w') as out_file:
        for slice_idx in range(num_slices_per_volume):
            slice_file_name = f"{volume_name}_slice_{slice_idx}.h5"
            slice_file_path = os.path.join(input_directory, slice_file_name)
            print(f"Slice {slice_idx} yapılıyor .")
            if os.path.exists(slice_file_path):
                with h5py.File(slice_file_path, 'r') as in_file:
                    # Her slice için ayrı bir grup oluştur
                    slice_group = out_file.create_group(f"slice_{slice_idx:03d}")
                    for key in in_file.keys():
                        in_file.copy(key, slice_group)
            else:
                print(f"File {slice_file_name} does not exist.")
                continue

print("All volumes combined into separate .h5 files.")