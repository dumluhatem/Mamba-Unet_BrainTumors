def split_volumes(input_file, output_file1, output_file2):
    all_volumes = set()
    existing_volumes = set()

    # slices_list.txt dosyasından mevcut olan volumeleri ayır
    with open(input_file, 'r') as f:
        for line in f:
            if line.strip():  # Satır boş değilse devam et
                volume = line.strip().split('_')[1]  # volume_X_slice_Y -> X al
                existing_volumes.add(volume)

    # Tüm volumeleri kümesine ekle (1'den 369'a kadar olan volumeler)
    all_volumes = set(str(vol) for vol in range(1, 370))

    # slices_list.txt dosyasında olmayan volumeleri bul
    non_existing_volumes = all_volumes - existing_volumes

    # %33'ünü output_file1'e yaz
    with open(output_file1, 'w') as f1:
        num_volumes1 = int(len(non_existing_volumes) * 0.33)
        for volume in sorted(non_existing_volumes)[:num_volumes1]:
            f1.write(f"volume_{volume}\n")

    # %66'sını output_file2'ye yaz
    with open(output_file2, 'w') as f2:
        num_volumes2 = int(len(non_existing_volumes) * 0.66)
        for volume in sorted(non_existing_volumes)[num_volumes1:num_volumes1 + num_volumes2]:
            f2.write(f"volume_{volume}\n")

# Örnek olarak slices_list.txt dosyasından volumeleri çıkarıp non_existing_volumes.txt ve small_non_existing_volumes.txt dosyalarına yazabiliriz
split_volumes('slices_list.txt', 'non_existing_volumes.txt', 'small_non_existing_volumes.txt')