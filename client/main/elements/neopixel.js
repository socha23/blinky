import * as api from '../services/neopixelApi'

function neopixel(state, setState) {

    function on() {
        api.on(state.id);
        setState({...state, setting: "on"})
    }

    function off() {
        api.off(state.id);
        setState({...state, setting: "off"})
    }

    function setBrightness(val) {
        api.brightness(state.id, val);
        setState({...state, brightness: val})
    }


    return {
        name: () => state.name,
        setting: () => state.setting,
        brightness: () => state.brightness,
        on,
        off,
        setBrightness,
    }
}

export default neopixel