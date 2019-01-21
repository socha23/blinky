import fetch from 'isomorphic-fetch'

let state = {};
let subscribers = {};
let subscribersCount = 0;
let intervalHandler = null;

const REFRESH_RATE_MS = 10000;

function subscribe(id, onChange) {
    subscribers[id] = onChange;
    if (subscribersCount == 0) {
        intervalHandler = setInterval(loadServerData, REFRESH_RATE_MS);
        loadServerData();
    }
    subscribersCount++
}

function unsubscribe(id) {
    delete subscribers[id];
    subscribersCount--;
    if (subscribersCount === 0) {
        clearInterval(intervalHandler)
    }
}

function setState(aState) {
    state = aState;
    notifySubscribers()
}

function notifySubscribers() {
    for (let id in subscribers) {
        subscribers[id](state)
    }
}

function loadServerData() {
    fetch("/state")
        .then(function (response) {
            if (response.status >= 400) {
                throw new Error("Bad response from server");
            }
            return response.json();
        }).then(json => {
            setState(json);
    })
}

module.exports = {
    subscribe: subscribe,
    unsubscribe: unsubscribe,
    setState: setState
}

