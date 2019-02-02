import React, {useEffect, useState} from 'react'
import * as MachineState from "../services/machineState";
import neopixel from "./neopixel";

export const useNeopixels = () => {
    const [state, setState] = useState([]);
    useEffect(() => {
        const sub = MachineState.subscribe(() => {setState(MachineState.getState().neopixels)});
        return () => {
            MachineState.unsubscribe(sub)
        }
    }, []);
    return state;
};

export const useNeopixel = (idx) => {
    const [state, setState] = useState(MachineState.getNeopixelState(idx));
    useEffect(() => {
        const sub = MachineState.subscribe(() => {setState(MachineState.getNeopixelState(idx))});

        return () => {
            MachineState.unsubscribe(sub)
        }
    }, []);

    const newSetState = (state) => {MachineState.setNeopixelState(idx, state)};
    return neopixel(state, newSetState);
};

