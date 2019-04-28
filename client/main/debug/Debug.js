import React from 'react'
import {useDebug} from "./debugHooks";
import {rgbToHex, valuesToHex} from "../services/colorUtils";

const Debug = () => {
    const state = useDebug();
    return <div>
        <h1>Debug</h1>
        {state.leds.map((s, idx) =>
            <Led key={idx} {...s}/>)}
        {state.neopixels.map((s, idx) =>
            <Neopixel key={idx} {...s}/>)}
    </div>
};



const Led = ({name, value}) => <div style={{display: "flex", alignItems: 'center'}}>
    <RGBBulb r={value} g={value} b={value}/>
    <h2>LED {name}</h2>
</div>;

const Neopixel = ({name}) => <div>
    <h2>Neopixel {name}</h2>
</div>;

const RGBBulb = ({r, g, b}) => {
    console.log(r, g, b);
    const color = valuesToHex(r, g, b);
    console.log(color);
    return <div style={{
        width: 40,
        height: 40,
        backgroundColor: color,
        borderRadius: 20
    }}/>
};



export default Debug
