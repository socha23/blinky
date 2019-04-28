import * as api from '../services/ledApi'
import * as componentApi from '../services/componentApi'

function led(state, setState) {

    function on() {
        componentApi.on(state.pin);
        setState({...state, setting: "on"})
    }

    function off() {
        componentApi.off(state.pin);
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

export default led