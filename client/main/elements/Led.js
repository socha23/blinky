import * as api from '../services/ledApi'

function Led(state, setState) {

    function on() {
        api.on(state.pin);
        setState({...state, setting: "on"})
    }

    function off() {
        api.off(state.pin);
        setState({...state, setting: "off"})
    }

    function blink() {
        api.blink(state.pin);
        setState({...state, setting: "blink"})
    }

    function pulse() {
        api.pulse(state.pin);
        setState({...state, setting: "pulse"})
    }

    function setValue(val) {
        api.pwm(state.pin, val);
        setState({...state, value: val})
    }

    return {
        name: () => state.name,
        pin: () => state.pin,
        setting: () => state.setting,
        value: () => state.value,
        on: on,
        off: off,
        blink: blink,
        pulse: pulse,
        setValue: setValue,
    }
}

export default Led