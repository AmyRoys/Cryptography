def brute_force(ciphertext):
    # Define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Try all possible shifts
    for shift in range(26):
        plaintext = ''

        # Shift each character in the ciphertext
        for char in ciphertext:
            if char.isalpha():
                index = (alphabet.index(char) - shift) % len(alphabet)
                plaintext += alphabet[index]
            else:
                plaintext += char

        # Print the plaintext for this shift
        print(f'Shift {shift}: {plaintext.lower()}')

# Call the function with your ciphertext
brute_force('xkazxbpxoppmfofqoxkdfkdcloobsbkdbtfqexqbyvefppfabzljbelqcoljebiipexiifkqebpbzlkcfkbptfqexjlkxozepslfzbzovexslzxkaibqpifmqebaldplctxo')
#Shift 23: andcaesarsspiritrangingforrevengewithatebyhissidecomehotfromhellshallintheseconfineswithamonarchsvoicecryhavocandletslipthedogsofwar