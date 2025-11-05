file = open ("day 1-20.txt","r")
buffer = file.readlines()
print(buffer)
file.close()
MSFT=[]
AMZN=[]
NVDA=[]
MSFTline = buffer [0].strip().split(f",")
AMZNline =buffer [0].strip().split(f",")
NVDAline =buffer [0].strip().split(f",")
print(MSFTline)
print(AMZNline)
print(NVDAline)