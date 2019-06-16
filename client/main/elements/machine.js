import * as api from '../services/machineApi'

class Machine {

    constructor(state, updateState, stateCallback) {
        this.state = {...state};
        this._updateState = updateState;
        this._stateCallback = stateCallback;
    }

    turnOn = () => {
        api.on(this._stateCallback);
        this._updateState({on: true})
    };

    turnOff = () => {
        api.off(this._stateCallback);
        this._updateState({on: false})
    };

    get name() {
        return this.state.name
    }

    get on() {
        return this.state.on
    }
}

export default Machine