# The set of characters we support
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet += "1234567890"
alphabet += " !@#$%^&*()-_+=`~;:'[]{}|<>,./?"
alphabet += "\"\\"

# How many characters we have
character_count = len(alphabet)

# List all our supported characters
print("Supported Characters:\n" + alphabet + "\n")

def encrypt_character(plain, key):
  # Turn plain character and key character into number codes
  key_code = alphabet.index(key)
  plain_code = alphabet.index(plain)

  # Combine plain + key, and loop back to zero at character_count
  cipher_code = (key_code + plain_code) % character_count
  
  # Turn cipher_code back into a character
  cipher = alphabet[cipher_code]

  # Done. Return our ciphertext character
  return cipher

def encrypt(plain, key):
  cipher = ""

  # Loop over every character in our plaintext
  for (plain_index, plain_character) in enumerate(plain):
    # Use the index of our plain character to get the corresponding key character
    key_index = plain_index % len(key)
    key_character = key[key_index]

    # Encrypt our plain character with our key character
    cipher_character = encrypt_character(key_character, plain_character)

    # Add our new cipher character to the end of our ciphertext
    cipher += cipher_character

  # Done. Return our full ciphertext
  return cipher

def invert_character(character):
  # Turn our character into a number code
  character_code = alphabet.index(character)

  # Get the "opposite" character in our alphabet
  inverted_code = (character_count - character_code) % character_count
  inverted_character = alphabet[inverted_code]

  return inverted_character

def invert(key):
  inverted_key = ""
  
  # Loop over every character in key, invert it, and add it to our inverted key
  for character in key:
    inverted_key += invert_character(character)

  return inverted_key

while True:
  plaintext = input("Message: ")
  key = input("Password: ")

  # Is our message already encrypted?
  encrypted = plaintext.startswith("!")

  # If so, remove the first character from plaintext (!), and invert the key
  if encrypted:
    plaintext = plaintext[1:]
    key = invert(key)

  ciphertext = encrypt(plaintext, key)

  # If not, put a ! character to the beginning so we know it's already encrypted
  if not encrypted:
    ciphertext = "!" + ciphertext

  print("Output: " + ciphertext + "\n")