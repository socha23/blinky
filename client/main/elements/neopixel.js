import * as api from '../services/neopixelApi'
import * as componentApi from '../services/componentApi'

class Neopixel {

    constructor(state, setState) {
        this.state = {...state};
        this.setState = setState;
    }

    setStateFromOutside(newState) {
        this.state = newState
    }

    turnOn = () => {
        componentApi.on(this.state.id);
        this.setState({...this.state, on: true})
    };

    turnOff = () => {
        componentApi.off(this.state.id);
        this.setState({...this.state, on: false})
    };

    fire = () => {
        api.fire(this.state.id);
        this.setState({...this.state, setting: "fire", on: true})
    };

    rgb = (params = {r: 0.5, g: 0.5, b: 0.5}) => {
        api.rgb(this.state.id, params);
        this.setState({...this.state, setting: "rgb", params, on: true});
    };

    effect = (params = {body: 'constant(1),constant(1),constant(1)'}, onSuccess, onFailure) => {
        api.effect(this.state.id, params, onSuccess, onFailure);
        this.setState({...this.state, setting: "effect", params, on: true});
    };

    rainbow = (params = {speed: 0.5}) => {
        api.rainbow(this.state.id, params);
        this.setState({...this.state, setting: "rainbow", params, on: true});
    };

    setParam(name, value, onSuccess, onFailure) {
        const newParams = {...this.state.params};
        newParams[name] = value;
        switch(this.state.setting) {
            case "rgb":
                this.rgb(newParams);
                break;
            case "rainbow":
                this.rainbow(newParams);
                break;
            case "effect":
                this.effect(newParams, onSuccess, onFailure);
                break;

        }
    }

    get name() {
        return this.state.name
    }

    get setting() {
        return this.state.setting
    }

    get brightness() {
        return this.state.brightness
    }

    set brightness(val) {
        api.brightness(this.state.id, val);
        this.setState({...this.state, brightness: val})
    }

    get params() {
        return this.state.params
    }

    get on() {
        return this.state.on
    }
}

export default Neopixel