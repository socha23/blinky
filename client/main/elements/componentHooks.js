import React, {useEffect, useState} from 'react'
import fetch from "isomorphic-fetch";
import Component from "./component";

const REFRESH_RATE_MS = 10000;

const INITIAL_STATE = {
    leds: [],
    neopixels: [],
};

const useMachineModel = () => {
    const [state, setState] = useState(INITIAL_STATE);
    useEffect(() => {
        const handler = setInterval(() => {
            updateStateFromServer(setState)
            }, REFRESH_RATE_MS);
        updateStateFromServer(setState);
        return () => {
            clearInterval(handler)
        }
    }, []);
    return makeModel(state, setState);
};

function updateStateFromServer(setState) {
    fetch("/state")
        .then(r => r.json())
        .then(state => {setState(state)});
}

function makeModel(state, setState) {
    const model = {leds: [], neopixels: [], devicesById: {}, deviceTypes: {}};
    fillModelDeviceType(model, state, setState, "leds", "led");
    fillModelDeviceType(model, state, setState, "neopixels", "neopixel");
    return model;
}

function fillModelDeviceType(model, state, setState, deviceCollection, deviceType) {
    state[deviceCollection].forEach(deviceState => {
        const stateSetter = (newDeviceState) => {
            const newState = {...state};
            newState[deviceCollection] = state[deviceCollection].map(s => s.id == newDeviceState.id ? newDeviceState : s);
            setState(newState);
        };
        const component = new Component(deviceState, stateSetter);
        model[deviceCollection].push(component);
        model.devicesById[component.id] = component;
        model.deviceTypes[component.id] = deviceType;
    })
}

export default useMachineModel


