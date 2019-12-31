import heapq

# Open file from folder
tt = open("dracula.txt", "r",encoding="utf8")
string1=tt.read().replace('\n','')
data = ''
# considering only ascii characters from 32 to 128
for char in string1:
    if ord(char) > 31 and ord(char) < 129:
        data += char
# encodes freq table for weight and symbol. Lowest two 
# numbers are taken from priority queue and stored. 
# function returns sorted list with frequencies of symbols
def encode(freq):
    heap = [[weight, [symbol, '']] for symbol, weight in freq.items()]
    
    heapq.heapify(heap)
    
    while len(heap) > 1:
        num1 = heapq.heappop(heap)
        
        num2 = heapq.heappop(heap)
       
        for pair in num1[1:]:
            pair[1] = '0' + pair[1]
           
        for pair in num2[1:]:   
            pair[1] = '1' + pair[1]
            
        heapq.heappush(heap, [num1[0] + num2[0]] + num1[1:] + num2[1:])
       

    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

# counting number of characters
freq = {}
for symbol in data:
    
    if symbol in freq:
        
        freq[symbol] += 1
        
    else:
        freq[symbol] = 1
       
huff = encode(freq)
huffcode = 0

for p in huff:
    
    print(p[0].ljust(10) +":"+ p[1])
 
    huffcode += freq[p[0]]*len(p[1])
# to calculate the original and comrpessed bits
print("ORIGINAL STRING",len(data)*7) 
print("COMPRESSED CODE",huffcode)

