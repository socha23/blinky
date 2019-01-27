import * as api from '../services/fireApi'

function fire(state, setState) {

    function on() {
        api.on(state.id);
        setState({...state, setting: "on"})
    }

    function off() {
        api.off(state.id);
        setState({...state, setting: "off"})
    }

    function setIntensity(intensity) {
        api.intensity(state.id, intensity);
        setState({...state, intensity: intensity})
    }

    return {
        name: () => state.name,
        setting: () => state.setting,
        intensity: () => state.intensity,
        setIntensity,
        on,
        off,
    }
}

export default fire