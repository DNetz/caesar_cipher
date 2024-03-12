import click
from caesar_cipher.cipher import encrypt, decrypt, brute_force

@click.command()
@click.option('--infile', type=click.File('r'), help='Input file path.', required=True)
@click.option('--outfile', type=click.File('w'), help='Output file path.', required=True)
@click.option('--encrypt', 'mode', flag_value='encrypt', help='Encrypt the content of the input file.')
@click.option('--decrypt', 'mode', flag_value='decrypt', help='Decrypt the content of the input file.')
@click.option('--brute-force', 'mode', flag_value='brute_force', help='Attempt to decrpyt the contents of the input file via brute-force.')
@click.option('--shift', default=1, help='Number of positions to shift by. Required for encryption and decryption.', show_default=True)

def main(infile, outfile, mode, shift):
    """Process the input file and writes the result to the output file based on the selected mode."""
    
    text = infile.read()

    if mode == 'encrypt':
        result = encrypt(text, shift)
    elif mode == 'decrypt':
        result = decrypt(text, shift)
    elif mode == 'brute_force':
        result = "\n".join([f"Shift {i}: {brute_force(text, i)}" for i in range(26)])
    else:
        raise click.UsageError("You must specify either --encrypt, --decrypt, or --brute-force.")

    outfile.write(result)
    click.echo(f"Processed file saved to {outfile.name}")

if __name__ == '__main__':
    main()
