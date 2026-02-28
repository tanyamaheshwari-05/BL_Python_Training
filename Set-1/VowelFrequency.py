sentence = input("Enter the Sentence : ")
sentence= sentence.lower()
count=0
for char in sentence:
    if(char == 'a' or char == 'e' or char== 'i' or char=='o' or char=='u' ):
        count+=1
print("Vowel count : ",count)