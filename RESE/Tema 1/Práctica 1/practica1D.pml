/*Propiedades LTL*/
ltl enciende_azul { [] ((tiempoT_azul && !luz_azul) -> <> luz_azul) }
ltl apaga_azul { [] ((tiempoT_azul && luz_azul) -> <> !luz_azul) }

ltl aliveON_azul { []<> tiempoT_azul -> []<> luz_azul }
ltl aliveOFF_azul { []<> tiempoT_azul -> []<> !luz_azul}

ltl enciende_roja { [] (boton -> <> luz_roja) }
ltl apaga_roja { [] (tiempoT_roja -> <> !luz_roja) }

ltl aliveON_roja { []<> boton -> []<> luz_roja }
ltl aliveOFF_roja { []<> tiempoT_roja -> []<> !luz_roja}


/*Estados, entradas, salidas*/
mtype = { BLINK, ON, OFF };
int luz_state;
int boton
int luz
int tiempoT


/*FSMs*/
active proctype luz_state {
    luz_state == OFF;
	do
	:: (luz_state==OFF) -> atomic {
		if
		:: boton -> luz=1; boton=0; luz_state = BLINK
		fi
	}

	:: (luz_state==BLINK) -> atomic {
		if
		:: tiempoT -> luz=!luz; tiempoT=0
		:: (boton && !tiempoT) -> luz=1; tiempoT=0; boton=0; luz_state==0N

		fi
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
        :: tiempoT = 1
        :: boton = 1
		:: skip -> skip
        fi;
		printf("luz_state_azul=%d, luz_azul=%d, tiempoT_azul=%d, tiempoT_roja=%d, luz_roja=%d, luz_state_roja=%d, boton=%d\n", 
       luz_state_azul, luz_azul, tiempoT_azul, tiempoT_roja, luz_roja, luz_state_roja, boton);

	od
}



