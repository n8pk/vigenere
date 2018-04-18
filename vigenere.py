import string
from collections import deque

class VigenereCipher:
    
    def __init__(self):
        
        self.characters = deque(string.printable)        
        
        
    def encrypt(self, plaintext, code):
        """Takes in a plaintext string and returns ciphertext"""
        
        self.rotation_sequence = [self.characters.index(char) for char in code]
        
        indices = [self.characters.index(letter) for letter in plaintext]
        
        new_indices = []
        for idx, num in enumerate(indices):
            codex = self.rotation_sequence[idx%len(self.rotation_sequence)]
            new_indices.append(num - codex)
        
        new_letters = [self.characters[i] for i in new_indices]
        
        return ''.join(new_letters)
        
    
    def decrypt(self, ciphertext, code):
        """Takes in a ciphertext string and returns plaintext"""
        
        self.rotation_sequence = [self.characters.index(char) for char in code]

        indices = [self.characters.index(letter) for letter in ciphertext]

        new_indices = []
        for idx, num in enumerate(indices):
            codex = self.rotation_sequence[idx%len(self.rotation_sequence)]
            new_indices.append(num + codex)
        
        new_letters = []
        for i in new_indices:
            check = len(self.characters)
            if i < check:
                new_letters.append(self.characters[i])
            else:
                new_letters.append(self.characters[i-check])
        
        return ''.join(new_letters)
