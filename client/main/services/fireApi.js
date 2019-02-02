import {putJson} from "./apiUtils";

export function on(id) {
    putJson(fireAddr(id) + "/on")
}

export function off(id) {
    putJson(fireAddr(id) + "/off")
}

export function intensity(id, intensity) {
    putJson(fireAddr(id) + "/intensity/" + intensity)
}

function fireAddr(id) {
    return "/fire/" + id
}

