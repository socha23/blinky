import fetch from 'isomorphic-fetch'

let subscribers = {};
let subscribersCount = 0;
let state = {leds: []};
let intervalHandler = null;


const REFRESH_RATE_MS = 10000;
let subNo = 0;

function subscribe(onChange) {
    subNo++;
    subscribers[subNo] = onChange;
    if (subscribersCount === 0) {
        intervalHandler = setInterval(loadServerData, REFRESH_RATE_MS);
        loadServerData();
    }
    subscribersCount++;
    return subNo
}

function unsubscribe(id) {
    delete subscribers[id];
    subscribersCount--;
    if (subscribersCount === 0) {
        clearInterval(intervalHandler)
    }
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
            state = json;
            notifySubscribers();
    })
}


function getLedState(idx) {
    return state.leds[idx]
}

function setLedState(idx, ledState) {
    state.leds[idx] = ledState;
    notifySubscribers()
}

module.exports = {
    subscribe: subscribe,
    unsubscribe: unsubscribe,
    getState: () => state,
    setLedState: setLedState,
    getLedState: getLedState,
};


