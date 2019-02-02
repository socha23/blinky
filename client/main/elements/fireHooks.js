import React, {useEffect, useState} from 'react'
import fire from "./fire";
import * as MachineState from "../services/machineState";

export const useFires = () => {
    const [state, setState] = useState([]);
    useEffect(() => {
        const sub = MachineState.subscribe(() => {setState(MachineState.getState().fires)});
        return () => {
            MachineState.unsubscribe(sub)
        }
    }, []);
    return state;
};

export const useFire = (idx) => {
    const [state, setState] = useState(MachineState.getFireState(idx));
    useEffect(() => {
        const sub = MachineState.subscribe(() => {setState(MachineState.getFireState(idx))});

        return () => {
            MachineState.unsubscribe(sub)
        }
    }, []);

    const newSetState = (state) => {MachineState.setFireState(idx, state)};
    return fire(state, newSetState);
};

