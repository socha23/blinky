import {putJson} from "./apiUtils";

export function on(stateCallback) {
    putJson("/on", {}, stateCallback)
}

export function off(stateCallback) {
    putJson("/off", {}, stateCallback)
}

