import fetch from 'isomorphic-fetch'

export function putJson(addr, obj = {}) {
    return fetch(addr, {
        method: 'PUT',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(obj)
    })
        .then(function (response) {
            if (response.status >= 400) {
                throw new Error("Bad response from server");
            }
            return response.json();
        })
}

