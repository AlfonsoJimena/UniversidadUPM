/*Propiedades LTL*/
ltl enciende { [] (boton -> <> luz) }
ltl apaga { [] (tiempoT -> <> !luz) }

ltl aliveON { []<> boton -> []<> luz }
ltl aliveOFF { []<> tiempoT -> []<> !luz}


/*Estados, entradas, salidas*/
mtype = { OFF, ON };
int luz_state;
int boton;
int luz;
int tiempoT


/*FSMs*/
active proctype luz_fsm() {
	luz_state=OFF;
	do
	:: (luz_state==OFF) -> atomic {
		if
		:: boton -> luz=1; boton=0; luz_state = ON
		fi
	}

	:: (luz_state==ON) -> atomic {
		if
		:: (boton && !tiempoT) -> boton=0; luz_state = ON
        :: tiempoT -> luz=0; tiempoT=0; luz_state = OFF
		fi
	}
	od
}

/*entorno*/
active proctype entorno() {
	do
	:: 	if
		:: boton=1
        :: tiempoT = 1
		:: skip -> skip
		fi; printf("luz_state=%e, boton=%d, luz=%d\n, tiempoT", luz_state, boton, luz, tiempoT)
	od
}