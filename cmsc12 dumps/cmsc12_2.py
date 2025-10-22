#reverse RLE, from compressed to decompressed 

def rle_reverse(rle_compressed):
    tokens = rle_compressed.split(",") 
    digit = 0
    bitmap_row = ""

    for t in tokens:
        for i in range(0, int(t)):
            bitmap_row += str(digit)
        digit = (digit+1)%2
    return bitmap_row

def decompressedBitmap(compressed_bitmap):
    bitmap_image = []
    for bitmap_row in compressed_bitmap:
        bitmap_image.append(rle_reverse(bitmap_row))
    return bitmap_image

def printFunc(list1):
    for e in list1:
        print(e)

compressed_bitmap = ['3,1,1,3,1,1,2', '4,4,4']
bitmap_image = decompressedBitmap(compressed_bitmap)
printFunc(compressed_bitmap)
printFunc(bitmap_image)

# comp_result = compressedBitImage(testList)
# printFunc(testList)
# print(f"\nRLE-compressed bitmap image:")
# printFunc(comp_result)
