;run 'python main.py test.asm N'
;where N is some value
;program will calculate sum of 1 + 2 + ... + N
;in registers r2 and r3
;by default N = 5

ldm 12        ; acc = 12
end:

                    ; call custom subroutine for:
jms $3ff            ; printing regs
jms $3fd            ; printMemory(4, 16)
