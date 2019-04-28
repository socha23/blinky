import * as api from '../services/fireApi'
import * as componentApi from '../services/componentApi'

function fire(state, setState) {

    function on() {
        componentApi.on(state.id);
        setState({...state, setting: "on"})
    }

    function off() {
        componentApi.off(state.id);
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