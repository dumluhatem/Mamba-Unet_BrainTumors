def generate_slices_list(volume_start, volume_end, slice_count):
    with open('all_slices.list', 'w') as f:
        for volume in range(volume_start, volume_end + 1):
            for slice_num in range(slice_count):
                f.write(f"volume_{volume}_slice_{slice_num}\n")

# Örnek olarak volume 1'den 369'a kadar ve slice 0'dan 154'e kadar olan listeyi oluşturabiliriz
generate_slices_list(1, 369, 155)