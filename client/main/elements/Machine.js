import Led from './Led'

function Machine(state, setState) {

    function setLedState(idx) {
        return ledState => {
            const newLeds = [...state.leds];
            newLeds[idx] = ledState;
            setState({...state, leds: newLeds});
        }
    }
    return {
        leds: state.leds.map((ledState, idx) => Led(ledState, setLedState(idx))
        )
    }
}

export default Machine