import {putJson} from "./apiUtils";

export function on(id) {
    putJson(componentAddr(id) + "/on")
}

export function off(id) {
    putJson(componentAddr(id) + "/off")
}

function componentAddr(id) {
    return "/component/" + id
}

