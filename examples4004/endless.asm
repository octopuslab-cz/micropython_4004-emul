; input/output acc + sleep, endless loop
; 2021 - OctopusLab - for #EDU_KIT1
;--------------------------------------------

start:
jms $3f1        ; input4 to acc + sleep
jms $3f0        ; output acc to exp8 + sleep
jms $3ff        ; printing regs

main_loop:
dac             ; acc -= 1
jms $3f0        ; output acc + sleep
jcn az start    ; if acc == 0 jump to start again
jun main_loop   ; jump to main_loop

end:
nop             ; no operation
          


