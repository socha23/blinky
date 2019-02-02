import React, {useEffect, useState} from 'react'
import * as MachineState from "../services/machineState";
import neopixels from "./neopixels";

export const useAllNeopixels = () => {
    const [state, setState] = useState([]);
    useEffect(() => {
        const sub = MachineState.subscribe(() => {setState(MachineState.getState().neopixels)});
        return () => {
            MachineState.unsubscribe(sub)
        }
    }, []);
    return state;
};

export const useNeopixels = (idx) => {
    const [state, setState] = useState(MachineState.getNeopixelsState(idx));
    useEffect(() => {
        const sub = MachineState.subscribe(() => {setState(MachineState.getNeopixelsState(idx))});

        return () => {
            MachineState.unsubscribe(sub)
        }
    }, []);

    const newSetState = (state) => {MachineState.setNeopixelsState(idx, state)};
    return neopixels(state, newSetState);
};

