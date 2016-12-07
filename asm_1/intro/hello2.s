global _start

section .text
_start:
	; sys_write(stdout, message, length)
	mov     rax, 1         ; write
	mov     rdi, 1         ; stdout
	mov     rsi, msg
	mov     rdx, msglen
  syscall

	; sys_exit(return_code)
	mov     rax, 60        ; exit
	mov     rdi, 0         ; ret code
  syscall


section .data
msg:     db      `Hello,\n multiline asm!\n`, 0
msglen:  equ     $ - msg
