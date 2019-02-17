import React, {useEffect, useState} from 'react'
import * as MachineState from "../services/machineState";
import Neopixel from "./neopixel";

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
    const npxMachineState = MachineState.getNeopixelState(idx);
    const setNpxMachineState = (state) => {MachineState.setNeopixelState(idx, state)};

    const [npx, setNpx] = useState(new Neopixel(npxMachineState, setNpxMachineState));

    useEffect(() => {
        const sub = MachineState.subscribe(() => {
            const newNpxState = MachineState.getNeopixelState(idx);
            npx.setStateFromOutside(newNpxState);
            setNpx(npx)
        });

        return () => {
            MachineState.unsubscribe(sub)
        }
    }, []);
    return npx;
};

