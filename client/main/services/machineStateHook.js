import {useEffect, useState} from 'React'

import * as MachineState from './machineState'

export const useMachine = () => {
    const [state, setState] = useState({leds: []});
    useEffect(() => {
        MachineState.subscribe(0, setState);

        return () => {
            MachineState.unsubscribe(0)
        }
    });
    return Machine(state, setState)
};

function Machine(state, setState) {

    function setLedState(idx) {
        return ledState => {
            const newLeds = [...state.leds];
            newLeds[idx] = ledState;
            setState({...state, leds: newLeds});
        }
    }

    return {
        leds: state.leds.map((ledState, idx) => Led(ledState, setLedState(idx))
        )
    }
}

function Led(state, setState) {
    return {
        name: state.name
    }
}
