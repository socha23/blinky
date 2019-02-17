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
    onClick={() => {neopixel[setting]()}}
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
    <table>
        <tbody>
        <tr>
            <td>R</td>
            <td style={{paddingBottom: 5}}><ParamSlider neopixel={neopixel} paramName={'r'}/></td>
        </tr>
        <tr>
            <td>G</td>
            <td style={{paddingBottom: 5}}><ParamSlider neopixel={neopixel} paramName={'g'}/></td>
        </tr>
        <tr>
            <td>B</td>
            <td style={{paddingBottom: 5}}><ParamSlider neopixel={neopixel} paramName={'b'}/></td>
        </tr>
        </tbody>
    </table>
    <hr/>
</div>;

const RainbowParams = ({neopixel}) => <div style={{marginBottom: 5}}>
    <h5>Speed:</h5>
    <ParamSlider neopixel={neopixel} paramName={'speed'}/>
    <hr/>
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