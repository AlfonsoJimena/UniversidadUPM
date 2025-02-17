/*Estados, entradas, salidas*/
mtype = { OFF, ON };
int luz_state;
int boton;
int luz;

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
		:: boton -> luz=0; boton=0; luz_state = OFF
		fi
	}
	od
}

/*entorno*/
active proctype entorno() {
	do
	:: 	if
		:: boton=1
		:: skip -> skip
		fi; printf("luz_state=%e, boton=%d, luz=%d\n", luz_state, boton, luz)
	od
}
