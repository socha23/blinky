import {putJson} from "./apiUtils";

export function blink(pin) {
    putJson(ledAddr(pin) + "/blink")
}

export function pulse(pin) {
    putJson(ledAddr(pin) + "/pulse")
}

export function pwm(pin, val) {
    putJson(ledAddr(pin) + "/pwm/" + val)
}

function ledAddr(pin) {
    return "/led/" + pin
}

