/*Propiedades LTL*/
ltl enciende { [] ((tiempoT && !luz) -> <> luz) }
ltl apaga { [] ((tiempoT && luz) -> <> !luz) }

ltl aliveON { []<> tiempoT -> []<> luz }
ltl aliveOFF { []<> tiempoT -> []<> !luz}


/*Estados, entradas, salidas*/
mtype = { toggle };
int luz_state;
int luz;
int tiempoT


/*FSMs*/
active proctype luz_fsm() {
	luz_state=toggle;
	do
	:: (luz_state==toggle) -> atomic {
		if
		:: tiempoT -> luz=!luz;tiempoT = 0; luz_state = toggle
		fi   
	}
    od
}

/*entorno*/
active proctype entorno() {
	do
	:: 	if
        :: tiempoT = 1
		:: skip -> skip
		fi; printf("luz_state=%e, luz=%d\n, tiempoT",luz_state, luz, tiempoT)
	od
}