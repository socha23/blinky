import {putJson} from "./apiUtils";

export function setting(setting, id, params={}, onSuccess, onFailure) {
    putJson(neopixelAddr(id) + "/setting/" + setting, params, onSuccess, onFailure)
}

export function brightness(id, val) {
    putJson(neopixelAddr(id) + "/brightness/" + val)
}

function neopixelAddr(id) {
    return "/neopixel/" + id
}


