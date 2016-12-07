global _start

section .text
_start:
	; sys_write(stdout, message, length)
	mov     rax, 1         ; write
	mov     rdi, 1         ; stdout
	mov     rsi, msg
	mov     rdx, msglen
  syscall

section .data
msg:     db      "Hello darkness, my old friend", 10, 0 ; 10 == '\n'
msglen:  equ     $ - msg
