import {putJson} from "./apiUtils";

export function on(id) {
    putJson(componentAddr(id) + "/on")
}

export function off(id) {
    putJson(componentAddr(id) + "/off")
}

export function setSetting(setting, id, params={}, onSuccess, onFailure) {
    putJson(componentAddr(id) + "/setting/" + setting, params, onSuccess, onFailure)
}

export function updateParams(id, params, onSuccess, onFailure) {
    putJson(componentAddr(id) + "/params", params, onSuccess, onFailure)
}

function componentAddr(id) {
    return "/component/" + id
}

