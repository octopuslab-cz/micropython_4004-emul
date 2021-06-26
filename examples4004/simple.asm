;ldm + print reg + sllep basic test

jms $3f1	 ; input4 to acc + sleep
xch r0           ; store it to r0
jms $3f0	 ; output acc to exp8 + sleep

ldm 7            ; acc = 7
jms $3f0         ; output acc + sleep
iac		 ; increment Accumulator
jms $3f0         ; output acc + sleep 
ld r0            ; acc = r0


main_loop:
dac              ; acc -= 1
jms $3f0         ; output acc + sleep
jcn az end       ; if acc == 0 jump to end 
jun main_loop    ; jump to main_loop
          
end:

                 ; call custom subroutine for:
jms $3fc         ; sleep
jms $3ff         ; printing regs
jms $3fd         ; printMemory(4, 16)
