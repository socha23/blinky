import fetch from 'isomorphic-fetch'

function ledAddr(pin) {
    return "/led/" + pin
}

function turnOn(pin) {
    putJson(ledAddr(pin) + "/on")
}

function turnOff(pin) {
    putJson(ledAddr(pin) + "/off")
}

export default function led(pin) {
    return {
        on: () => turnOn(pin),
        off: () => turnOff(pin),
    }
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