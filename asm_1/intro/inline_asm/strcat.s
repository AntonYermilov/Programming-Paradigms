global strcat_asm

section .data
a: dd 1

section .text
strcat_asm:
  mov rax, rdi
  ; TODO: implement me

end:
	ret
