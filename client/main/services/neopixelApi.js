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

export function effect(id, params, onSuccess, onFailure) {
    setting(id, "effect", params, onSuccess, onFailure);
}

export function rainbow(id, params) {
    setting(id, "rainbow", params);
}

function neopixelAddr(id) {
    return "/neopixel/" + id
}

function setting(id, setting, params={}, onSuccess, onFailure) {
    putJson(neopixelAddr(id) + "/" + setting, params, onSuccess, onFailure)
}

export function brightness(id, val) {
    putJson(neopixelAddr(id) + "/brightness/" + val)
}

