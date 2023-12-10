# Python_Final_Assignment
Text encryption/decryption


**Description:**

The code will take a word or message inputted from the user and encrypt it to a key and write it to a file specified by that user. It can also decrypt the message with the provided key and file name, it then prints the now decrypted message.
The encryption works when the user inputs the arguments for encryption (--encrypt) and enters the message, a new random key is made from the generate_key() function. A Fernet cipher suite is then created using that key (A cipher suite is turning that secret message into code and back.) The message is then turned into bytes, the script then returns the key (the bytes) used for encryption/decryption. The code uses symmetric encryption so that only the same key and filename can be used to decrypt the encrypted message. The file that is created is stored in the same directory as the script unless the file path is specified, so keep in mind when you try and call a file. To decrypt the file you need to use the decryption argument (--decrypt) with the file name/path and key that was created in the encryption process.


**Dependencies:**

In order to run the script you will need to have the cryptography module installed, you can do that by doing -pip install cryptography


**Usage Guide:**
You must be in the same directory of the script in order for it to run!
There are arguments that are required in order to run the script properly, they are "--encrypt", "--decrypt", "--file" and "--key" these are also listed in the "How to run" section of this readme.
When encrypting and decryptig please keep in mind that when doing the --file parameter you must type a valid file path and make the file a .txt. If not the script will error out telling you that the path or extension is not vaild.
As well when entering your secret message there must be a value entered or you won't be able to encrypt, the script will notify you saying there is no message and you must enter something to continue.
If you forget the key to decrypt it, open the file in the file explorer and it will show the key. Once the argument is entered the script will validate if the path and key match and if it does it will print the message, if not it will display an error message.


**How to run:**

- To encrypt: python3 Corbin_Assignment.py --encrypt --file _Insert File Name Here_

- To decrypt: python3 Corbin_Assignment.py --decrypt --file _Insert File Name/path Here_ --key _Insert Key Here_


**References:**

- https://cryptography.io/en/latest/fernet/
- https://pypi.org/project/cryptography/
- https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/
- https://pythonistaplanet.com/fernet/
- https://chat.openai.com/
