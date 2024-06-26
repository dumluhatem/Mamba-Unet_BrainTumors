
def extract_unique_volumes(input_file, output_file):
    volumes = set()

    # Dosyayı oku ve unique volumeleri topla
    with open(input_file, 'r') as f:
        for line in f:
            volume = line.strip().split('_')[1]  # volume_X_slice_Y -> X al
            volumes.add(volume)

    # Unique volumeleri yaz
    with open(output_file, 'w') as f:
        for volume in sorted(volumes, key=int):  # Volumeleri sırala (sayıya göre)
            f.write(f"volume_{volume}\n")

# Örnek olarak slices_list.txt dosyasından volumeleri çıkarıp volumes_selected.txt dosyasına yazabiliriz
extract_unique_volumes('slices_list.txt', 'volumes_selected.txt')