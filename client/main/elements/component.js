import * as api from '../services/componentApi'

class Component {

    constructor(state, updateState) {
        this.state = {...state};
        this._updateState = updateState;
        this.lastApiParamUpdate = new Date()
    }

    turnOn = () => {
        api.on(this.state.id);
        this._updateState({on: true})
    };

    turnOff = () => {
        api.off(this.state.id);
        this._updateState({on: false})
    };

    setSetting = (name, params = {}, onSuccess, onFailure) => {
        api.setSetting(name, this.state.id, params, onSuccess, onFailure);
        this._updateState({setting: name})
    };

    updateParam(name, value) {
        this.setParam(name, value, true);
    }

    setParam(name, value, forceApiUpdate = false, apiUpdateInterval = 200) {
        this._updateState({params: {...this.state.params, [name]: value}});
        if (forceApiUpdate || new Date() - this.lastApiParamUpdate > apiUpdateInterval) {
            this.lastApiParamUpdate = new Date();
            const params = {};
            params[name] = value;
            api.updateParams(this.state.id, params);
        }
    }

    get id() {
        return this.state.id
    }

    get name() {
        return this.state.name
    }

    get setting() {
        return this.state.setting
    }

    get params() {
        return this.state.params
    }

    get on() {
        return this.state.on
    }

    get type() {
        return this.state.type
    }
}

export default Component