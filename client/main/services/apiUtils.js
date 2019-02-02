import fetch from 'isomorphic-fetch'

export function putJson(addr) {
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

