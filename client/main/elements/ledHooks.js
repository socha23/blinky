import React, {useEffect, useState} from 'react'
import Component from "./component";
import * as MachineState from "../services/machineState";

export const useLeds = () => {
    const [state, setState] = useState([]);
    useEffect(() => {
        const sub = MachineState.subscribe(() => {setState(MachineState.getState().leds)});
        return () => {
            MachineState.unsubscribe(sub)
        }
    }, []);
    return state;
};

export const useLed = (idx) => {
    const [state, setState] = useState(MachineState.getLedState(idx));
    useEffect(() => {
        const sub = MachineState.subscribe(() => {setState(MachineState.getLedState(idx))});

        return () => {
            MachineState.unsubscribe(sub)
        }
    }, []);

    const newSetState = (state) => {MachineState.setLedState(idx, state)};
    return Component(state, newSetState);
};

