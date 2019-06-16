import React, {useEffect, useState} from 'react'
import fetch from "isomorphic-fetch";
import Component from "./component";
import Machine from "./machine";

const REFRESH_RATE_MS = 10000;

const INITIAL_STATE = {
    components: [],
};

export const useMachineModel = () => {
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
    const model = {
        components: [],
        componentsById: {}
    };
    const mergeComponentState = (compId) => {
        return (newCompState) => {
            const newComponents = state.components.map(oldCompState => {
                if (oldCompState.id == compId) {
                    return {...oldCompState, ...newCompState}
                } else {
                    return oldCompState
                }
            });
            setState({...state, components: newComponents});
        }
    };
    state.components.forEach(compState => {
        const component = new Component(compState, mergeComponentState(compState.id));
        model.components.push(component);
        model.componentsById[component.id] = component;
    });
    model.machine = new Machine(state.machine, (newMachineState) => {
        const newState = {...state, machine: {...state.machine, ...newMachineState}};
        setState(newState)
    }, setState);
    return model;
}
