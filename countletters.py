import pprint
message="sample script to count characters in a given message"
cnt={}

for character in message:
    cnt.setdefault(character,0)
    cnt[character]=cnt[character]+1

pprint.pprint(cnt)
    