import fetch from 'isomorphic-fetch'

export function on(pin) {
    putJson(ledAddr(pin) + "/on")
}

export function off(pin) {
    putJson(ledAddr(pin) + "/off")
}

export function blink(pin) {
    putJson(ledAddr(pin) + "/blink")
}

export function pulse(pin) {
    putJson(ledAddr(pin) + "/pulse")
}

function putJson(addr) {
    return fetch(addr, {
        method: 'PUT',
        //headers: {
        //    'Content-Type': 'application/json'
        //},
    })
        .then(function (response) {
            if (response.status >= 400) {
                throw new Error("Bad response from server");
            }
            return response.json();
        })
}

function ledAddr(pin) {
    return "/led/" + pin
}

