CLS	; clear screen

LD V9,#01	; used for SUB
LD VA,#00	; x position
LD VB,#00	; y position
LD VD,#00	; line break counter

;;; draw the string pin:
call nextline
LD V8,#00
LD I,str_pass	; address of string
LD V0,[I]	; read first byte = number of characters
LD VC,V0
loop:
LD I,str_pass
ADD V8,#01
ADD I,V8
LD V0,[I]	; read character offset index
call drawchar
SE VC,#00	; skip JP if done
JP loop

;;; get PIN
LD V1,K
LD V0,#28	; *
call drawchar
LD V2,K
LD V0,#28	; *
call drawchar
LD V3,K
LD V0,#28	; *
call drawchar
LD V4,K
LD V0,#28	; *
call drawchar

;;; draw the flag
call nextline
call nextline
LD V5,#00	; counter for XOR with pin
LD V8,#00
LD I,str_flag	; address of string
LD V0,[I]	; read first byte = number of characters
LD VC,V0
floop:
LD I,str_flag
ADD V8,#01
ADD I,V8
LD V0,[I]	; read character offset index
;; deobfuscation algo
;; xor with V1, V2, V3, V4 
SE V5,#00
JP c2
XOR V0,V1
XOR V0,V3
JP xorinc
c2:
SE V5,#01
JP c3
XOR V0,V2
XOR V0,V4
JP xorinc
c3:
SE V5,#02
JP c4
XOR V0,V3
XOR V0,V1
JP xorinc
c4:
SE V5,#03
JP xorinc
XOR V0,V4
XOR V0,V1
LD V5,#00
JP xordone
xorinc:
ADD V5,#01
xordone:
call drawchar
SE VC,#00	; skip JP if done
JP floop
JP end

end:
JP end

;;; draw sprite character and linebreak if needed
drawchar:
call drawsprite
SUB VC,V9	; count
ADD VA,#06	; increase x pos
ADD VD,#01	; line break count
SNE VD,#0b	
JP nextline
RET
nextline:
LD VA,#00	; set x pos = 0
ADD VB,#06	; increase y pos
LD VD,#00	; reset line break counter
RET

;;; Draw a sprite
drawsprite:
LD I,#500
LD VE,#05
mul:
SNE V0,#00
JP draw
ADD I,VE
SUB V0,V9
JP mul
draw:
DRW VA,VB,05
RET
str_pass: db #04, #0f, #08, #0d, #27 ; pin:
;str_flag: db #16, #02, #11, #00, #13, #04, #02, #13, #05, #24, #02, #07, #1b, #0f, #22, #26, #07, #1e, #02, #0a, #1d, #03, #25 ; cratectf{ch1p8_h4ck3d}
; PIN=2357
str_flag: db #16, #05, #15, #07, #16, #03, #06, #14, #00, #23, #06, #00, #1e, #08, #26, #21, #02, #19, #06, #0d, #18, #04, #21 ; cratectf{ch1p8_h4ck3d}

offset #500

db			; a
	%00000000,
	%00110000,
	%01010000,
	%01010000,
	%00111000

db			; b
	%01000000,
	%01000000,
	%01110000,
	%01001000,
	%01110000

db			; c
	%00000000,
	%00111000,
	%01100000,
	%01100000,
	%00111000

db			; d
	%00001000,
	%00001000,
	%00111000,
	%01001000,
	%00111000

db			; e
	%00110000,
	%01001000,
	%01110000,
	%01000000,
	%00111000

db			; f
	%00111000,
	%00100000,
	%01110000,
	%00100000,
	%00100000

db			; g
	%00110000,
	%01001000,
	%00111000,
	%00001000,
	%00110000

db			; h
	%01000000,
	%01000000,
	%01110000,
	%01001000,
	%01001000

db			; i
	%00100000,
	%00000000,
	%00100000,
	%00100000,
	%00100000

db			; j
	%00010000,
	%00000000,
	%00010000,
	%00010000,
	%00110000

db			; k
	%01000000,
	%01000000,
	%01010000,
	%01100000,
	%01010000

db			; l
	%00100000,
	%00100000,
	%00100000,
	%00100000,
	%00110000

db			; m
	%00000000,
	%00000000,
	%00101000,
	%01010100,
	%01010100

db			; n
	%00000000,
	%01000000,
	%01110000,
	%01001000,
	%01001000

db			; o
	%00000000,
	%00000000,
	%00110000,
	%01001000,
	%00110000

db			; p
	%00110000,
	%01001000,
	%01110000,
	%01000000,
	%01000000

db			; q
	%00110000,
	%01001000,
	%00111000,
	%00001000,
	%00001000

db			; r
	%00000000,
	%00111000,
	%01000000,
	%01000000,
	%01000000

db			; s
	%00111000,
	%01000000,
	%00110000,
	%00001000,
	%01110000

db			; t
	%00100000,
	%01110000,
	%00100000,
	%00100000,
	%00111000

db			; u
	%00000000,
	%01001000,
	%01001000,
	%01001000,
	%01111000

db			; v
	%00000000,
	%01001000,
	%01001000,
	%01001000,
	%00110000

db			; w
	%00000000,
	%10000100,
	%10000100,
	%10110100,
	%01001000

db			; x
	%00000000,
	%00000000,
	%01001000,
	%00110000,
	%01001000

db			; y
	%00000000,
	%01001000,
	%01111000,
	%00001000,
	%00111000

db			; z
	%01111000,
	%00001000,
	%00110000,
	%01000000,
	%01111000

db			; 0
	%01111000,
	%01001000,
	%01001000,
	%01001000,
	%01111000

db			; 1
	%00010000,
	%00110000,
	%00010000,
	%00010000,
	%00111000

db			; 2
	%01111000,
	%00001000,
	%01111000,
	%01000000,
	%01111000

db			; 3
	%01111000,
	%00001000,
	%01111000,
	%00001000,
	%01111000

db			; 4
	%01001000,
	%01001000,
	%01111000,
	%00001000,
	%00001000

db			; 5
	%01111000,
	%01000000,
	%01111000,
	%00001000,
	%01111000

db			; 6
	%01111000,
	%01000000,
	%01111000,
	%01001000,
	%01111000

db			; 7
	%01111000,
	%00001000,
	%00010000,
	%00100000,
	%00100000

db			; 8
	%01111000,
	%01001000,
	%01111000,
	%01001000,
	%01111000

db			; 9
	%01111000,
	%01001000,
	%01111000,
	%00001000,
	%01111000

db			; {
	%00011000,
	%00110000,
	%01100000,
	%00110000,
	%00011000

db			; }
	%01100000,
	%00110000,
	%00011000,
	%00110000,
	%01100000

db			; _
	%00000000,
	%00000000,
	%00000000,
	%00000000,
	%01111000

db			; :
	%00000000,
	%00110000,
	%00000000,
	%00110000,
	%00000000

db			; *
	%00000000,
	%00010000,
	%00111000,
	%00010000,
	%00000000
