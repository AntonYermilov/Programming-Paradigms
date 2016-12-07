global _start

section .text
_start:
  mov     rbx, msg        ; move the address of our message string into rbx
  mov     rax, rbx        ; move the address in RBX into RAX as well (Both now point to the same segment in memory)

nextchar:
  cmp     byte [rax], 0   ; compare the byte pointed to by RAX at this address against zero (Zero is an end of string delimiter)
  jz      finished        ; jump (if the zero flagged has been set) to the point in the code labeled 'finished'
  inc     rax             ; increment the address in RAX by one byte (if the zero flagged has NOT been set)
  jmp     nextchar        ; jump to the point in the code labeled 'nextchar'

finished:
  sub     rax, rbx        ; subtract the address in RBX from the address in RAX
  ; remember both registers started pointing to the same address (see line 6)
  ; but RAX has been incremented one byte for each character in the message string
  ; when you subtract one memory address from another of the same type
  ; the result is number of segments between them - in this case the number of bytes

	; sys_write(stdout, message, length)
	mov     rsi, msg
	mov     rdx, rax
	mov     rax, 1         ; write
	mov     rdi, 1         ; stdout
  syscall

	; sys_exit(return_code)
	mov     rax, 60        ; exit
	mov     rdi, 0         ; ret code
  syscall


section .data
msg:     db      `Hello, branching in asm!\n\0`
