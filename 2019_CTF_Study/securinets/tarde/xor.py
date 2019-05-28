while(1):
	org = int(raw_input(),16)
	key = ord(raw_input())

	print org, " ^ " ,key

	ans = org^key
	print chr(ans)
