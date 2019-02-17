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
                    <SettingButton neopixel={neopixel} setting='on' className={"btn-primary"}>On</SettingButton>
                    <SettingButton neopixel={neopixel} setting='rgb' className={"btn-info"}>RGB</SettingButton>
                    <SettingButton neopixel={neopixel} setting='rainbow' className={"btn-info"}>Rainbow</SettingButton>
                    <SettingButton neopixel={neopixel} setting='fire' className={"btn-info"}>Fire</SettingButton>
                    <SettingButton neopixel={neopixel} setting='off' className={"btn-danger"}>Off</SettingButton>
                </div>
            </div>
        </div>
    </div>
};

const SettingButton = ({className, children, neopixel, setting}) => <button
    style={{marginRight: 6}}
    onClick={() => {
        neopixel[setting]()
    }}
    className={"btn " + className + (neopixel.setting === setting ? " active" : "")}>
    {children}
</button>;


const BrightnessSlider = ({neopixel}) => <div style={{marginBottom: 5}}>
    <Slider
        value={neopixel.brightness}
        onChange={v => {
            neopixel.brightness = v
        }}
    />
    <hr/>
</div>;


const SettingParams = ({neopixel}) => {
    switch (neopixel.setting) {
        case "rgb":
            return <RGBParams neopixel={neopixel}/>
        case "rainbow":
            return <RainbowParams neopixel={neopixel}/>
        default:
            return <div/>
    }
};


const RGBParams = ({neopixel}) => <div>
    <RGBSlider neopixel={neopixel} caption='R' param='r'/>
    <RGBSlider neopixel={neopixel} caption='G' param='g'/>
    <RGBSlider neopixel={neopixel} caption='B' param='b'/>
    <hr/>
</div>;


const RGBSlider = ({neopixel, caption, param}) => <div>
    <div style={{display: "flex", marginBottom: 15}}>
        <span>{caption}</span>
        <div style={{flexGrow: 1}}>
            <ParamSlider neopixel={neopixel} paramName={param}/>
        </div>
    </div>
</div>;


const RainbowParams = ({neopixel}) => <div style={{marginBottom: 5}}>
    <h5>Speed:</h5>
    <ParamSlider neopixel={neopixel} paramName={'speed'} min={-1}/>
    <hr/>
</div>;


const ParamSlider = ({neopixel, paramName, min=0}) => {
    return <Slider
        value={neopixel.params[paramName]}
        onChange={v => {
            neopixel.setParam(paramName, v)
        }}
        min={min}
    />
};


const Slider = ({value, onChange, min=0}) => {
    return <ReactBootstrapSlider
        value={value}
        change={e => {
            onChange(e.target.value)
        }}
        step={0.01}
        min={min}
        max={1}
    />
};

export default NeopixelBox