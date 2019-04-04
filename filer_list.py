i = [{'host':'1.1.1.1','port':8888,'protocol':'http'},{'host':'1.1.1.2','port':8888,'protocol':'http'},{'host':'1.1.1.3','port':8888,'protocol':'http'}]

i = list(filter(lambda x:x['host'] != '1.1.1.2',i))

print(i)


aa,bb = 'hello','world'
strs = '{} {}'.format(aa,bb)
print(strs)