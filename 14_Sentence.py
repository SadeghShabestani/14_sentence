sentence = input("Enter Sentence: ")

print(f"Len: {len(sentence)}")

while True:
    if sentence == "exit":
        break
    else:
        sentence = input("Enter Sentence: ")
        print(f"Len: {len(sentence)}")
