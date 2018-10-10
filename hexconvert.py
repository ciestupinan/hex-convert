"""Convert a hexadecimal string, like '1A', into it's decimal equivalent.

    >>> hex_convert('6')
    6

    >>> hex_convert('10')
    16

    >>> hex_convert('FF')
    255

    >>> hex_convert('FFFF')
    65535
"""


def hex_convert(hex_in):
    """Convert a hexadecimal string, like '1A', into it's decimal equivalent."""
    base_ten_num = 0

    reversed_hex_in = hex_in[::-1]


    for i in range(len(reversed_hex_in)):
    	
    	# base_ten_num = base_ten_num + (reversed_hex_in * pow(16,i))
    	if reversed_hex_in[i].lower() == 'a':
    		base_ten_num = base_ten_num + (10 * pow(16,i))
    	elif reversed_hex_in[i].lower() == 'b':
    		base_ten_num = base_ten_num + (11 * pow(16,i))
    	elif reversed_hex_in[i].lower() == 'c':
    		base_ten_num = base_ten_num + (12 * pow(16,i))
    	elif reversed_hex_in[i].lower() == 'd':
    		base_ten_num = base_ten_num + (13 * pow(16,i))
    	elif reversed_hex_in[i].lower() == 'e':
    		base_ten_num = base_ten_num + (14 * pow(16,i))
    	elif reversed_hex_in[i].lower() == 'f':
    		base_ten_num = base_ten_num + (15 * pow(16,i))
    	else:
    		base_ten_num = base_ten_num + (int(reversed_hex_in[i]) * pow(16,i))

    return base_ten_num

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. YOU'RE TERRIFIC!\n")
