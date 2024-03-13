import time

matched_word = "Hello World !"
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', 
              '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', 
              '{', '}', '|', '\\', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', ' ']

final_match = ''

for i in range(len(matched_word)):
    found = False
    for char in characters:
        if char == matched_word[i]:
            final_match += char
            time.sleep(0.05)
            found = True
            break
        else:
            print(final_match + char)
            time.sleep(0.05)
print(f"{final_match}\n" * 10)
print("\n\n\nFinal Matched:", final_match)
