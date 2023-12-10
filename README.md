# Python_Final_Assignment
Text encryption/decryption
Description:

The code will take a word or message inputted from the user and encrypt it to a key and write it to a file specified by that user. It can also decrypt the message with the provided key and file name it then prints the now decrypted message.
The encryption works when the user inputs the arguments for encryption and enters the message, a new random key is made using the generate_key() function. A Fernet cipher suite is then created using this key (A cipher suite is turning that secret message into code and back.) The message is then turned into bytes, the script then returns the key used for encryption. The code uses symmetric encryption so that only the same key and filename can be used to decrypt the encrypted message. The file that is created is stored in the same directory as the script, so keep in mind when you try and call a file. If you move the file out of the directory/file the script will not be able to decrypt it if you call for it.

Dependencies:

- pip
- pip install cryptography

Commands to run:

To encrypt: python3 Corbin_Assignment.py --encrypt --file _Insert File Name Here_

To decrypt: python3 Corbin_Assignment.py --decrypt --file _Insert File Name Here_--key _Insert Key Here_


References:

- https://cryptography.io/en/latest/fernet/
- https://pypi.org/project/cryptography/
- https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/
- https://pythonistaplanet.com/fernet/
- Edge Copilot
