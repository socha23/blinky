import {putJson} from "./apiUtils";

export function setSetting(setting, id, params={}, onSuccess, onFailure) {
    putJson(neopixelAddr(id) + "/setting/" + setting, params, onSuccess, onFailure)
}

export function updateParams(id, params) {
    putJson(neopixelAddr(id) + "/params", params)
}

function neopixelAddr(id) {
    return "/neopixel/" + id
}


