import React from 'react'
import useMachineModel from "../elements/componentHooks"
import Neopixel from "./Neopixel";
import Led from "./Led";

const Main = () => {
    const model = useMachineModel();
    return <div>
        {model.leds.map(led =>
            <Led key={led.id} component={led}/>)}
        {model.neopixels.map(px =>
            <Neopixel key={px.id} component={px}/>)}
    </div>
};

export default Main