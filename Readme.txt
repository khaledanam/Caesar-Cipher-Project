>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Custom Caesar Cipher Project <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
> Description of Caesar Cipher:
Its a simple encryption decryption method that generally works in three steps. Usually works around the 26 alphabets from A to Z. Maybe Uppercase or maybe Lowercase.
Each of the alphabets hold indexing from 0 to last (eg: 25). Based upon the indexing and alphabetic order the encryption and decryption takes place.

--> Encryption:
1. Takes input from the user. (Plain text)
2. Shifts each of the letter 3 times including the starting letter. (Plain text: HELLO. so the encrypted text: KHOOR). H,I,J->K. E,F,G-> H. L,M,N->O. L,M,N->O. O,P,Q-> R. = KHOOR.
3. Encrypted Output text.

--> Decryption:
1. Takes encrypted input from the user. (encrypted text)
2. Reverses each letter 3 times including the starting letter as 0 index.(encrypted text: KHOOR. so the decrypted text: HELLO). K,J,I-> H. H,G,F->E. O,N,M->L. O,N,M->L. R,Q,P->O. = HELLO.
3. Decrypted Output text.


> Description of Custom Caesar Cipher :
The base of this custom software is as usual as the general caesar cipher formula. But it has some extra features. Features are mentioned below:

1. When encrypting texts, User can input the Array of Alphabets, Numerics, Special Characters. (its not limited to the sequntial order. like abcdefgh...)
2. User can shift key n times. (not limited to 3 shift) .Of course bound to the total number of arrays.
3. The custom array and shift key generates an additional config file. 
4. After taking the plain text inputs from user, the software shuffles the word's order in the encrypted file. (eg: HELLO WORLD -> WORLD HELLO)
5. Then saves the encrypted file to the directory. 
6. While decrypting the file, user requires the initial config file in the directory to decrypt this file. 



