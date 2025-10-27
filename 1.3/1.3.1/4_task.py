def artificial_muscle_fibers(arr):
    byte_array = bytearray(8192)
    duplicate_elements = 0
    for item in arr:
        bit_position = item - 1
        byte_index = bit_position //8
        bit_index = bit_position % 8
        eight_bit_mask = 1 << bit_index
        if byte_array[byte_index] & eight_bit_mask:
            duplicate_byte_index = byte_index + 4000
            if not (byte_array[duplicate_byte_index] & eight_bit_mask):
                duplicate_elements +=1
                byte_array[duplicate_byte_index] |= eight_bit_mask
        else:
            byte_array[byte_index] |= eight_bit_mask
    return duplicate_elements