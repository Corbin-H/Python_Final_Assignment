import argparse
from cryptography.fernet import Fernet
#cryptography.fernet import Fernet is the module you import to do encryption, using symmetric encryption.

def generate_key():
    return Fernet.generate_key()
#This generates the encryption key when --encrypt is the arguement

def encrypt_message(message):
    key = generate_key()
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message, key
#Encodes the inputed message using message.encode() and then encrypts it using the Fernet object's encrypt method.

def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message
#Decrypts the message using Fernet and decodes the result to a string using .decode()

def write_to_file(file_path, content):
    with open(file_path, 'wb') as file:
        file.write(content)
#Takes the file in binary write mode and writes the provided message to a file.

def read_from_file(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
    return content
#This is used for reading encrypted data from a file.

def main():
    parser = argparse.ArgumentParser(description='Encrypt/decrypt messages with the cryptography.fernet module.')
    parser.add_argument('--encrypt', action='store_true', help='Encrypt the message and write it to a file')
    parser.add_argument('--decrypt', action='store_true', help='Read the message from a file and decrypt it')
    parser.add_argument('--file', type=str, help='File path for reading/writing messages')
    parser.add_argument('--key', type=str, help='Encryption/decryption key')

    args = parser.parse_args()
#If --encrypt is specified, it should encrypt a message using the key provided and write the encrypted message to a file specified by --file.
#If --decrypt is specified, it should read an encrypted message from a file specified by --file and decrypt it using the key provided by --key.

    if args.encrypt:
        message = input('Type a message to encrypt: ')
        encrypted_message, key = encrypt_message(message)
        file_path = args.file or 'default_encrypted_message.txt'
        write_to_file(file_path, encrypted_message)
        print(f'Message has been encrypted and saved to {file_path}. Key: {key.hex()}')
#If args is encrypt then it will ask for a message and file name to encrypt it with the key

    elif args.decrypt:
        if not args.key:
            print('Please provide a key using the --key option for decryption.')
            return
#If args is decrypt then it will ask for file name and key in the argument

        key = bytes.fromhex(args.key)
        file_path = args.file or 'default_encrypted_message.txt'
        encrypted_message = read_from_file(file_path)
        decrypted_message = decrypt_message(encrypted_message, key)
        print(f'The decrypted message from {file_path} is: {decrypted_message}')

    else:
        print('Please enter --encrypt or --decrypt. Thank you :)')
#This will print if --encrypt or --decrypt is not specified

if __name__ == '__main__':
    main()
