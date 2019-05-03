import * as api from '../services/componentApi'

class Component {

    constructor(state, setState) {
        this.state = {...state};
        this.setState = setState;
        this.lastApiParamUpdate = new Date()
    }

    setStateFromOutside(newState) {
        this.state = newState
    }

    turnOn = () => {
        api.on(this.state.id);
        this.setState({...this.state, on: true})
    };

    turnOff = () => {
        api.off(this.state.id);
        this.setState({...this.state, on: false})
    };

    setSetting = (name, params = {}, onSuccess, onFailure) => {
        api.setSetting(name, this.state.id, params, onSuccess, onFailure);
        this.setState({...this.state, setting: name, params: {...this.state.params, ...params}, on: true});
    };

    updateParam(name, value, onSuccess, onFailure) {
        this.setParam(name, value);
        api.updateParams(this.state.id, this.state.params, onSuccess, onFailure);
    }

    setParam(name, value, apiUpdateInterval = 200) {
        const params = {};
        params[name] = value;
        this.setState({...this.state, params: {...this.state.params, ...params}});
        if (new Date() - this.lastApiParamUpdate > apiUpdateInterval) {
            this.lastApiParamUpdate = new Date();
            api.updateParams(this.state.id, this.state.params);
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
}

export default Component