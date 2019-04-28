import * as api from '../services/componentApi'

class Neopixel {

    constructor(state, setState) {
        this.state = {...state};
        this.setState = setState;
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

    setParam(name, value) {
        const params = {};
        params[name] = value;
        api.updateParams(this.state.id, params);
        this.setState({...this.state, params: {...this.state.params, ...params}});
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

export default Neopixel