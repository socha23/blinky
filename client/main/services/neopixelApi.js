import {putJson} from "./apiUtils";

export function on(id) {
    putJson(neopixelAddr(id) + "/on")
}

export function off(id) {
    putJson(neopixelAddr(id) + "/off")
}

function neopixelAddr(id) {
    return "/neopixel/" + id
}

