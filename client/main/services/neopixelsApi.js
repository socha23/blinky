import {putJson} from "./apiUtils";

export function on(id) {
    putJson(neopixelsAddr(id) + "/on")
}

export function off(id) {
    putJson(neopixelsAddr(id) + "/off")
}

function neopixelsAddr(id) {
    return "/neopixels/" + id
}

