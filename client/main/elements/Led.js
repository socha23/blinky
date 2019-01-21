import * as api from '../services/ledApi'


function Led(state, setState) {


    function on() {
        api.on(state.pin);
        setState({...state, setting: "on", value: 1})
    }

    function off() {
        api.off(state.pin);
        setState({...state, setting: "off", value: 0})
    }

    function blink() {
        api.blink(state.pin);
        setState({...state, setting: "blink", value: 0})
    }

    function pulse() {
        api.pulse(state.pin);
        setState({...state, setting: "pulse", value: 0})
    }

    return {
        name: () => state.name,
        pin: () => state.pin,
        setting: () => state.setting,
        on: on,
        off: off,
        blink: blink,
        pulse: pulse,
    }
}

export default Led