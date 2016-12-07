global strcpy_asm

section .data
a: dd 2

section .text
strcpy_asm:
  mov rax, rdi

copy_loop:
  movsb
	cmp	byte [rsi], 0
	je	end
	jmp	copy_loop

end:
	ret
