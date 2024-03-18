import click
from caesar_cipher.cipher import encrypt, decrypt, brute_force

#Set up CLI options 
@click.command()
@click.option('--infile', type=click.File('r'), help='Input file path.', required=True)
@click.option('--outfile', type=click.File('w'), help='Output file path.', required=True)
@click.option('--encrypt', 'mode', flag_value='encrypt', help='Encrypt the content of the input file.')
@click.option('--decrypt', 'mode', flag_value='decrypt', help='Decrypt the content of the input file.')
@click.option('--brute-force', 'mode', flag_value='brute_force', help='Attempt to decrpyt the contents of the input file via brute-force.')
@click.option('--shift', default=1, help='Number of positions to shift by. Required for encryption and decryption.', show_default=True)

def main(infile, outfile, mode, shift):
    """Process the input file, shifts characters bases on the shift and mode arguments. Ends by writes the result to the output file."""
    # reads entire content of the input file into memory
    text = infile.read()

    # depending on the cli arguments, runs an encryption, decryption or brute force
    if mode == 'encrypt':
        result = encrypt(text, shift)
    elif mode == 'decrypt':
        result = decrypt(text, shift)
    elif mode == 'brute_force':
        # calls the brute_force function, returns the full text beginning with the shift amount used in each decryption atttempt.
        brute_force_results = brute_force(text)
        # each iteration starts with a new line, the shift amount and the decrpyted text
        result = "\n".join([f"Shift {s}: {decrypted_txt}\n" for s, decrypted_txt in brute_force_results])
    else:
        raise click.UsageError("You must specify either --encrypt, --decrypt, or --brute-force.")
    
    # writes the result of the above to the output file
    outfile.write(result)
    click.echo(f"Processed file saved to {outfile.name}")

# if present runs the 
if __name__ == '__main__':
    main()
