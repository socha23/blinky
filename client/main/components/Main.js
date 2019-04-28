import React from 'react'
import LedBox from "./LedBox";
import {useLeds} from "../elements/ledHooks";
import {useNeopixels} from "../elements/neopixelsHooks";
import Neopixel from "./Neopixel";

const Main = () => {
    const leds = useLeds();
    const neopixels = useNeopixels();
    return <div>
        {leds.map((_, idx) =>
            <LedBox key={idx} idx={idx}/>)}
        {neopixels.map((_, idx) =>
            <Neopixel key={idx} idx={idx}/>)}
    </div>
};

export default Main