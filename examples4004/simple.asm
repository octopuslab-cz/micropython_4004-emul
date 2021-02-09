;ldm + print reg + sllep basic test


jms $3fa	    ; input.reg to acc + sleep
xch r0              ; store it to r0
jms $3fa	    ; input.reg to acc + sleep
xch r1              ; store it to r1

ldm 7               ; acc = 7
jms $3fb            ; output acc + sleep
iac		    ; increment Accumulator
jms $3fb            ; output acc + sleep 

main_loop:
dac                 ; acc -= 1
jms $3fb            ; output acc + sleep
jcn az end          ; if acc == 0 jump to end 
jun main_loop       ; jump to main_loop
          
end:

                    ; call custom subroutine for:
jms $3fc            ; sleep
jms $3ff            ; printing regs
jms $3fd            ; printMemory(4, 16)
