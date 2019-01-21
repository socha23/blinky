import React, {useEffect, useState} from 'react'
import Main from "./components/Main";
import Machine from './elements/machine'
import * as MachineState from "./services/machineState";

const App = () => {
    const machine = useMachine();

    return <Main machine={machine}/>
};

const useMachine = () => {
    const INITIAL_STATE = {leds: []};
    const [state, setState] = useState(INITIAL_STATE);
    useEffect(() => {
        MachineState.subscribe(0, setState);

        return () => {
            MachineState.unsubscribe(0)
        }
    }, []);
    return Machine(state, setState)
};

export default App
