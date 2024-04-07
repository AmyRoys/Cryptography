def brute_force(ciphertext):
    # Define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet += alphabet.upper()

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
brute_force('Ykbxgwl, Khftgl, vhngmkrfxg, exgw fx rhnk xtkl; B vhfx mh unkr Vtxltk, ghm mh iktblx abf. Max xobe matm fxg wh eboxl tymxk maxf; Max zhhw bl hym bgmxkkxw pbma maxbk uhgxl. Lh exm bm ux pbma Vtxltk.')
#Shift 19: friends, romans, countrymen, lend me your ears; i come to bury caesar, not to praise him. the evil that men do lives after them; the good is oft interred with their bones. so let it be with caesar.