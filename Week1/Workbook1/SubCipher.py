from collections import Counter

def decrypt_substitution(ciphertext):
    # Define the English alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Count the frequency of each letter in the ciphertext
    counter = Counter(ciphertext)

    # Sort the letters by frequency
    sorted_letters = [letter for letter, count in counter.most_common()]

    # Define the frequency of each letter in English
    english_frequencies = 'etaoinshrdlcumwfgypbvkjxqz'

    # Create a mapping from the ciphertext letters to the English letters
    mapping = {cipher: plain for cipher, plain in zip(sorted_letters, english_frequencies)}

    # Decrypt the ciphertext
    plaintext = ''.join(mapping.get(char, char) for char in ciphertext)

    return plaintext

# Call the function with your ciphertext
print(decrypt_substitution('gsv tildgs lu xibkgltizksrx gvxsmloltb szh izrhvw z mfnyvi lu ovtzo rhhfvh rm gsv rmulinzgrlm ztv. xibkgltizksb\'h klgvmgrzo uli fhv zh z gllo uli vhkrlmztv zmw hvwrgrlm szh ovw nzmb tlevimnvmgh gl xozhhrub rg zh z dvzklm zmw gl ornrg li vevm kilsryrg rgh fhv zmw vcklig. rm hlnv qfirhwrxgrlmh dsviv gsv fhv lu xibkgltizksb rh ovtzo, ozdh kvinrg rmevhgrtzglih gl xlnkvo gsv wrhxolhfiv lu vmxibkgrlm pvbh uli wlxfnvmgh ivovezmg gl zm rmevhgrtzgrlm. xibkgltizksb zohl kozbh z nzqli ilov rm wrtrgzo irtsgh nzmztvnvmg zmw xlkbirtsg rmuirmtvnvmg wrhkfgvh drgs ivtziw gl wrtrgzo nvwrz.'))