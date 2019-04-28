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
    const npxMachineState = MachineState.getLedState(idx);
    const setNpxMachineState = (state) => {MachineState.setLedState(idx, state)};

    const [npx, setNpx] = useState(new Component(npxMachineState, setNpxMachineState));

    useEffect(() => {
        const sub = MachineState.subscribe(() => {
            const newNpxState = MachineState.getLedState(idx);
            npx.setStateFromOutside(newNpxState);
            setNpx(npx)
        });

        return () => {
            MachineState.unsubscribe(sub)
        }
    }, []);
    return npx;
};
