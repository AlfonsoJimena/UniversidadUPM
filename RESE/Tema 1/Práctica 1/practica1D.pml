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
mtype = { toggle, ON, OFF };
int luz_state_roja;
int luz_roja;
int tiempoT_roja;
int luz_state_azul;
int boton;
int luz_azul;
int tiempoT_azul;


/*FSMs*/
active proctype luz_roja_fsm() {
    luz_state_roja=OFF;
	do
	:: (luz_state_roja==OFF) -> atomic {
		if
		:: boton -> luz_roja=1; boton=0; luz_state_roja = ON
		fi
	}

	:: (luz_state_roja==ON) -> atomic {
		if
		:: (boton && !tiempoT_roja) -> boton=0; luz_state_roja = ON
        :: tiempoT_roja -> luz_roja=0; tiempoT_roja=0; luz_state_roja = OFF; printf("next=now+T")
		fi
	}
	od
}

active proctype luz_azul_fsm() {
	luz_state_azul=toggle;
	do
	:: (luz_state_azul==toggle) -> atomic {
		if
		:: tiempoT_azul -> luz_azul=!luz_azul;tiempoT_azul = 0; luz_state_azul = toggle; printf("next=next+T")
		fi   
	}
    od
}

/*entorno*/
active proctype entorno() {
	do
	:: 	if
        :: tiempoT_azul = 1
        :: tiempoT_roja = 1
        :: boton = 1
		:: skip -> skip
        fi;
		printf("luz_state_azul=%d, luz_azul=%d, tiempoT_azul=%d, tiempoT_roja=%d, luz_roja=%d, luz_state_roja=%d, boton=%d\n", 
       luz_state_azul, luz_azul, tiempoT_azul, tiempoT_roja, luz_roja, luz_state_roja, boton);

	od
}



