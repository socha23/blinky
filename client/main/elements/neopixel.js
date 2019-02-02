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

    return {
        name: () => state.name,
        setting: () => state.setting,
        on,
        off,
    }
}

export default neopixel