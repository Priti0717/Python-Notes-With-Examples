#indexing and slicing
city="Ahamadnagar"
print(city[3:6:1])
print(city[0:6:1])
print(city[-5:11:1])
print(city[-11:-4:3])
print(city[-8:-5:1])

media="instagram"
print(media[0:5:1])
print(media[-6:-3:1])
print(media[-1:-5:-1])
print(media[-5:-10:-2])
print(media[4:0:1]) # it gives us empty string
print(media[-3:11:1])
print(media[-3:11:-1])

name="priti jaysing patil"
print(name[::]) #priti jaysing patil
print(name[::-1])#litap gnisyaj itirp
print(name[6:-6:1])#jaysing
print(name[-5::1])#patil
print(name[::2])#piijyigptl
print(name[::-2])#ltpgiyjiip
print(name[-10:-6])#sing
print(name[5:-5:8])#empty space