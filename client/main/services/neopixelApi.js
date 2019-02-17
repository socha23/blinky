import {putJson} from "./apiUtils";

export function on(id) {
    setting(id, "on");
}

export function off(id) {
    setting(id, "off");
}

export function fire(id) {
    setting(id, "fire");
}

export function rgb(id, params) {
    setting(id, "rgb", params);
}

function neopixelAddr(id) {
    return "/neopixel/" + id
}

function setting(id, setting, params={}) {
    putJson(neopixelAddr(id) + "/" + setting, params)
}

export function brightness(id, val) {
    putJson(neopixelAddr(id) + "/brightness/" + val)
}

