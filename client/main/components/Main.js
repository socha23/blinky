import React from 'react'
import LedBox from "./LedBox";
import {useLeds} from "../elements/ledHooks";

const Main = () => {
    const leds = useLeds();
    return <div className={"container"} style={{marginTop: 30}}>
        <div className={"row"}>
            {leds.map((_, idx) =>
                <LedBox key={idx} idx={idx}/>)}
        </div>
    </div>
};

export default Main