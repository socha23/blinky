import fetch from 'isomorphic-fetch'

export function putJson(addr, obj = {}, onSuccess=()=>{}, onFailure=()=>{}) {
    return fetch(addr, {
        method: 'PUT',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(obj)
    })
        .then(r => {
            if (r.ok) {
                r.json().then(json => onSuccess(json), error => onFailure(error))
            } else {
                console.log("Bad response from server");
                r.json().then(json => onFailure(json), error => onFailure(error))
            }
        })
}

