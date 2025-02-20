ltl prop1 { [] ((!luz && boton) -> <> luz) }
ltl prop2 { [] (((luz_state==OFF) && boton) -> <> luz) }
ltl prop3 { [] (((luz_state==BLINK) && boton) -> <> luz) } 
ltl prop4 { [] (((luz_state==ON) && boton) -> <> !luz) } 
ltl prop5 { []<> boton -> []<> luz }
ltl prop6 { []<> boton -> []<> !luz } 
ltl prop7 { []((((luz_state==BLINK) W luz) && !luz && tiempoT) -> <>luz) } 
ltl prop8 { []((((luz_state==BLINK) W !luz) && luz && tiempoT) -> <>!luz) } 

/*Estados, entradas, salidas*/
mtype = { ON, OFF, BLINK };
int luz_state;
int luz;
int tiempoT;
int boton

/*FSMs*/
active proctype luz_fsm(){
    luz_state = OFF;
	do
	:: (luz_state==OFF) -> atomic {
		if
		:: boton -> luz=1; boton=0; luz_state=BLINK
		fi
	}
    :: (luz_state==BLINK) -> atomic {
        if
        :: (tiempoT && !boton) -> luz=!luz; tiempoT=0
        :: boton -> luz=1; boton=0; luz_state=ON
        fi
    }
    :: (luz_state==ON) -> atomic {
        if
        :: boton -> luz=0; boton=0; luz_state=OFF
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
        printf("luz_state=%e, boton=%d, luz=%d, tiempoT=%d\n", luz_state, boton, luz, tiempoT)
	od
}