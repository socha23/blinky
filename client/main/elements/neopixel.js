import * as api from '../services/neopixelApi'

class Neopixel {

    constructor(state, setState) {
        this.state = {...state};
        this.setState = setState;
    }

    setStateFromOutside(newState) {
        this.state = newState
    }

    on = () => {
        api.on(this.state.id);
        this.setState({...this.state, setting: "on"})
    };

    off = () => {
        api.off(this.state.id);
        this.setState({...this.state, setting: "off"})
    };

    fire = () => {
        api.fire(this.state.id);
        this.setState({...this.state, setting: "fire"})
    };

    rgb = (params = {r: 0.5, g: 0.5, b: 0.5}) => {
        api.rgb(this.state.id, params);
        this.setState({...this.state, setting: "rgb", params});
    };

    effect = (params = {body: '(0,0,0)'}, onSuccess, onFailure) => {
        api.effect(this.state.id, params, onSuccess, onFailure);
        this.setState({...this.state, setting: "effect", params});
    };

    rainbow = (params = {speed: 0.5}) => {
        api.rainbow(this.state.id, params);
        this.setState({...this.state, setting: "rainbow", params});
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
}

export default Neopixel