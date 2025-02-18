ltl enciende1 { [] ((tiempoT && !luz1) -> <> luz1) }
ltl apaga1 { [] ((tiempoT && luz1) -> <> !luz1) }

ltl aliveON1 { []<> tiempoT -> []<> luz1 }
ltl aliveOFF1 { []<> tiempoT -> []<> !luz1}

ltl enciende2 { [] (boton -> <> luz2) }
ltl apaga2 { [] (tiempoT2 -> <> !luz2) }

ltl aliveON2 { []<> boton -> []<> luz2 }
ltl aliveOF2F { []<> tiempoT2 -> []<> !luz2}



/*Estados, entradas, salidas*/
mtype = { OFF, ON, toggle };
int luz_state;
int luz1=0;
int luz2;
int tiempoT;
int tiempoT2;
int boton

/*FSMs*/
active proctype luz_fsm() {
    luz_state=OFF
	do
    :: (toggle) -> atomic {
        if
        :: tiempoT -> luz1=!luz1; tiempoT=0;
        fi
    }
	:: (luz_state==OFF) -> atomic {
		if
		::boton -> luz2=1; boton=0; luz_state=ON
		fi
	}
	:: (luz_state==ON) -> atomic {
		if
		:: (boton && !tiempoT2) ->boton=0; luz_state=ON
		:: tiempoT2 -> luz2=0; tiempoT2=0; luz_state=OFF
	}
	od
}

/*entorno*/
active proctype entorno() {
	do
	:: 	if
		:: tiempoT=1
		::tiempoT2=1
		:: boton=1
		:: skip -> skip
		fi; printf("boton=%d, tiempot2=%d, luz1=%d, luz2=%d, tiempoT=%d, tiempoT2=%d\n", 
		boton, tiempoT2, luz1, luz2, tiempoT)
	od
}



