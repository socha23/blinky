import React from 'react'
import {useDebug} from "./debugHooks";
import {valuesToHex} from "../services/colorUtils";

const Debug = () => {
    const state = useDebug();
    return <div>
        {state.components.map((s, idx) =>
            <DebugComponent key={idx} component={s}/>)}
    </div>
};

const DebugComponent = ({component}) => {
    switch (component.type) {
        case 'led':
            return <Led {...component}/>
        case 'neopixel':
            return <Neopixel {...component}/>
    }
};

const DeviceName = ({children}) => <span style={{
    fontSize: 30,
}}>{children}</span>;

const Led = ({name, value}) => <div style={{display: "flex", alignItems: 'center'}}>
    <RGBBulb r={value} g={value} b={value}/>
    <DeviceName>{name}</DeviceName>
</div>;

const Neopixel = ({name, value}) => <div style={{display: "flex", alignItems: 'center'}}>
    {
        value.map((v, idx) => <RGBBulb key={"bulb" + idx} r={v[0]} g={v[1]} b={v[2]}/>)
    }
    <DeviceName>{name}</DeviceName>
</div>;

const RGBBulb = ({r, g, b}) => {
    const color = valuesToHex(r, g, b);
    const shadow = valuesToHex(r * 0.5, g * 0.5, b * 0.5);
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
