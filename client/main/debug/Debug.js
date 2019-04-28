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


const DeviceName = ({children}) => <span style={{
    fontSize: 30,
}}>{children}</span>;

const Led = ({name, value}) => <div style={{display: "flex", alignItems: 'center'}}>
    <RGBBulb r={value} g={value} b={value}/>
    <DeviceName>{name}</DeviceName>
</div>;

const Neopixel = ({name}) => <div>
    <DeviceName>{name}</DeviceName>
</div>;

const RGBBulb = ({r, g, b}) => {
    const color = valuesToHex(r, g, b);
    const shadow = valuesToHex(r * 0.5, g * 0.5, b * 0.5);

    console.log(color);
    return <div style={{
        margin: 10,
        width: 40,
        height: 40,
        backgroundColor: color,
        background: "radial-gradient(circle at 10px 10px, " + color + ", " + shadow + ")",
        borderRadius: 20
    }}/>
};



export default Debug
