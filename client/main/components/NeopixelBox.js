import React from 'react'
import {useNeopixel} from "../elements/neopixelsHooks";
import ReactBootstrapSlider from "react-bootstrap-slider";


const NeopixelBox = ({idx}) => {
    const neopixel = useNeopixel(idx);

    return <div className={"col-sm-4"}>
        <div className="panel panel-default">
            <div className="panel-heading">
                <h3 className="panel-title">{neopixel.name}</h3>
            </div>

            <div className="panel-body">
                <BrightnessSlider neopixel={neopixel}/>
                <SettingParams neopixel={neopixel}/>
                <div>
                    <SettingButton active={neopixel.setting === "on"} className={"btn-primary"} onClick={neopixel.on}>On</SettingButton>
                    <SettingButton active={neopixel.setting === "rgb"} className={"btn-info"} onClick={() => {
                        neopixel.rgb()
                    }}>RGB</SettingButton>
                    <SettingButton active={neopixel.setting === "fire"} className={"btn-info"} onClick={neopixel.fire}>Fire</SettingButton>
                    <SettingButton active={neopixel.setting === "off"} className={"btn-danger"} onClick={neopixel.off}>Off</SettingButton>
                </div>
            </div>
        </div>
    </div>
};

const SettingButton = ({className, children, onClick, active}) => <button
    style={{marginRight: 6}}
    onClick={onClick}
    className={"btn " + className + (active ? " active" : "")}>
    {children}
</button>;


const BrightnessSlider = ({neopixel}) => <div style={{marginBottom: 5}}>
    <Slider
        value={neopixel.brightness}
        onChange={v => {
            neopixel.brightness = v
        }}
    />
</div>;


const SettingParams = ({neopixel}) => {
    switch (neopixel.setting) {
        case "rgb":
            return <RGBSettings neopixel={neopixel}/>
        default:
            return <div/>
    }
};


const RGBSettings = ({neopixel}) => <div>
    <table>
        <tbody>
        <tr>
            <td>R</td>
            <td><ParamSlider neopixel={neopixel} paramName={'r'}/></td>
        </tr>
        <tr>
            <td>G</td>
            <td><ParamSlider neopixel={neopixel} paramName={'g'}/></td>
        </tr>
        <tr>
            <td>B</td>
            <td><ParamSlider neopixel={neopixel} paramName={'b'}/></td>
        </tr>
        </tbody>
    </table>
</div>;


const ParamSlider = ({neopixel, paramName}) => {
    return <Slider
        value={neopixel.params[paramName]}
        onChange={v => {
            neopixel.setParam(paramName, v)
        }}
    />
};


const Slider = ({value, onChange}) => {
    return <ReactBootstrapSlider
        value={value}
        change={e => {
            onChange(e.target.value)
        }}
        step={0.01}
        min={0}
        max={1}
    />
};

export default NeopixelBox