'''
Codewars resistor puzzle
test.it("A resistor under 1000 ohms and with only three bands")   
test.assert_equals(decode_resistor_colors("yellow violet black"), "47 ohms, 20%")
test.it("A resistor between 1000 and 999999 ohms, with a gold fourth band")   
test.assert_equals(decode_resistor_colors("yellow violet red gold"), "4.7k ohms, 5%")
test.it("A resistor of 1000000 ohms or above, with a silver fourth band")   
test.assert_equals(decode_resistor_colors("brown black green silver"), "1M ohms, 10%")
'''
def decode_resistor_colors(bands):
    lookup = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "gray": 8,
        "white": 9
    }

    # If no fourth band default to 20% tolerance
    tol = 20
    total = 0
    for i, band in enumerate(bands.split()):
        print('band {}'.format(band))
        # Get first two digits
        if i < 2:
            total = (total * 10) + lookup[band]
        # multiply factor
        elif i == 2:
            total = total * (10 ** lookup[band])
        # Read tolerence band if there is one
        elif i == 3:
            if band == 'silver':
                tol = 10
            if band == 'gold':
                tol = 5

    if total >= 1000000:
        ret = '{}M ohms, {}%'.format(total//1000000, tol)
    elif total >= 1000:
        ret = '{}K ohms, {}%'.format(total/1000, tol)
    else:
        ret = '{} ohms, {}%'.format(total, tol)

    return ret

def main():
    '''
    Main entry point
    '''
    print(decode_resistor_colors("yellow violet black"))
    print(decode_resistor_colors("yellow violet red gold"))
    print(decode_resistor_colors("brown black green silver"))

if __name__ == "__main__":
    main()
