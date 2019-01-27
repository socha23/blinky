import fetch from 'isomorphic-fetch'

export function on(id) {
    putJson(fireAddr(id) + "/on")
}

export function off(id) {
    putJson(fireAddr(id) + "/off")
}

export function intensity(id, intensity) {
    putJson(fireAddr(id) + "/intensity/" + intensity)
}


function putJson(addr) {
    return fetch(addr, {
        method: 'PUT',
    })
        .then(function (response) {
            if (response.status >= 400) {
                throw new Error("Bad response from server");
            }
            return response.json();
        })
}

function fireAddr(id) {
    return "/fire/" + id
}

