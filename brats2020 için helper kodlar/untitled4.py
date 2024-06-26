import h5py
import os

input_directory = "/home/hatemdumlu/h5/slices"  # Slice dosyalarının bulunduğu dizin
output_directory = "/home/hatemdumlu/h5/output11"  # Birleştirilen dosyaların kaydedileceği dizin

os.makedirs(output_directory, exist_ok=True)

num_volumes = 369
num_slices_per_volume = 155

for volume_idx in range(1, num_volumes + 1):
    volume_name = f"volume_{volume_idx}"
    output_file = os.path.join(output_directory, f"{volume_name}.h5")
    print(f"Volume {volume_idx} işleniyor...")

    # Son slice dosyasının adını oluştur
    last_slice_idx = num_slices_per_volume - 1
    last_slice_file_name = f"{volume_name}_slice_{last_slice_idx}.h5"
    last_slice_file_path = os.path.join(input_directory, last_slice_file_name)

    if os.path.exists(last_slice_file_path):
        with h5py.File(last_slice_file_path, 'r') as last_slice_file:
            # Son slice dosyasındaki 'etiket' adlı dataset'i al
            if 'etiket' in last_slice_file:
                etiket_data = last_slice_file['etiket'][()]

                # Volume dosyasını açarak en sona 'label' adıyla dataset'i ekle
                with h5py.File(output_file, 'a') as volume_file:
                    volume_file.create_dataset('label', data=etiket_data)

    else:
        print(f"Dosya {last_slice_file_name} mevcut değil.")

    # Diğer slice dosyalarını işle
    with h5py.File(output_file, 'a') as volume_file:
        for slice_idx in range(num_slices_per_volume):
            slice_file_name = f"{volume_name}_slice_{slice_idx}.h5"
            slice_file_path = os.path.join(input_directory, slice_file_name)
            #print(f"Slice {slice_idx} işleniyor...")

            if os.path.exists(slice_file_path):
                with h5py.File(slice_file_path, 'r') as slice_file:
                    slice_group_name = f"slice_{slice_idx:03d}"
                    slice_group = volume_file.create_group(slice_group_name)
                    
                    for key in slice_file.keys():
                        slice_file.copy(key, slice_group)
            else:
                print(f"Dosya {slice_file_name} mevcut değil.")
                continue

print("Tüm volumeler ayrı .h5 dosyalarına birleştirildi.")
