import React from 'react'
import LedBox from "./LedBox";
import {useLeds} from "../elements/ledHooks";
import {useFires} from "../elements/fireHooks";
import FireBox from "./FireBox";
import {useNeopixels} from "../elements/neopixelsHooks";
import NeopixelBox from "./NeopixelBox";

const Main = () => {
    const leds = useLeds();
    const fires = useFires();
    const neopixels = useNeopixels();
    return <div className={"container"} style={{marginTop: 30}}>
        <div className={"row"}>
            {leds.map((_, idx) =>
                <LedBox key={idx} idx={idx}/>)}
            {fires.map((_, idx) =>
                <FireBox key={idx} idx={idx}/>)}
            {neopixels.map((_, idx) =>
                <NeopixelBox key={idx} idx={idx}/>)}
        </div>
    </div>
};

export default Main