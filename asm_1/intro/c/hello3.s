global main

extern printf

section .data
fmtStr:  db `hello, printf\n\0`

section .text
main:
  push    rbp                   ; set up stack frame, same as "sub rsp, 8; mov [rsp], rbp"

	mov	    rdi, fmtStr
  call    printf		            ; call C function

  pop     rbp                   ; restore stack, same as "mov rbp, [rsp]; add 8, rsp"

  xor     rax, rax              ; return value
	ret
