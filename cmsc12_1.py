#create a function that performs RLE on a given bit map image repped by string of 1's and 0's
    
def rle(bitmap_row):
    if not bitmap_row:
        return []
    compressed = ""
    binary_digit = bitmap_row[0]
    count = 1
    for i in range(1, len(bitmap_row)):
        c = bitmap_row[i]
        if binary_digit == c:
            count += 1
        else:
            compressed = compressed + str(count) + ","
            binary_digit = c
            count = 1
    compressed = compressed + str(count)
    return compressed

def compressedBitImage(image):
    compressed_bitmap = []
    for bitmap_row in image:
        compressed_bitmap.append(rle(bitmap_row))
    return compressed_bitmap

def printFunc(list):
    for e in list:
        print(e)


testList = ["111100001101", 
            "000011110000", 
            "000101110100",
            "000000100000",
            "100100111000"]


comp_result = compressedBitImage(testList)
printFunc(testList)
print(f"\nRLE-compressed bitmap image:")
printFunc(comp_result)
