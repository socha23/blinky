import React, {useState} from 'react'
import {useNeopixel} from "../elements/neopixelsHooks";
import {BrightnessSlider, ComponentBox, ParamSlider, SettingButton} from "./elements";

const Neopixel = ({idx}) => {
    const neopixel = useNeopixel(idx);
    return <ComponentBox component={neopixel}>
        <SettingsBox neopixel={neopixel}/>
    </ComponentBox>
};

const SettingsBox = ({neopixel}) => <div style={{width: "100%", padding: 10, marginBottom: 10}}>
    <BrightnessSlider component={neopixel}/>
    <div style={{marginTop: 30, marginBottom: 10, display: "flex", justifyContent: "space-between"}}>
        <SettingButton component={neopixel} setting='rgb' icon={"glyphicon glyphicon-menu-hamburger"}/>
        <SettingButton component={neopixel} setting='rainbow' icon={"glyphicon glyphicon-heart"}/>
        <SettingButton component={neopixel} setting='fire' icon={"glyphicon glyphicon-fire"}/>
        <SettingButton component={neopixel} setting='effect' icon={"glyphicon glyphicon-wrench"}/>
    </div>
    <SettingParams neopixel={neopixel}/>
</div>;

const SettingParams = ({neopixel}) => {
    switch (neopixel.setting) {
        case "effect":
            return <EffectParams neopixel={neopixel}/>;
        case "rgb":
            return <RGBParams neopixel={neopixel}/>;
        case "rainbow":
            return <RainbowParams neopixel={neopixel}/>;
        default:
            return <div/>
    }
};

const EffectParams = ({neopixel}) => {
    const [body, setBody] = useState("(0,0,0)");
    const [error, setError] = useState(null);

    const onSuccess = () => {
        setError(null);
    };

    const onFailure = (msg) => {
        setError(msg);
        console.error(msg);
    };

    return <div>
        {error ? <div className={"text-danger"}>{error}</div> : <div/>}
        <textarea className={"form-control"} value={body} onChange={e => setBody(e.target.value)}/>
        <button
            className={"btn btn-block btn-lg btn-success"}
            style={{marginTop: 10}}
            onClick={e => neopixel.updateParam("body", body, onSuccess, onFailure)}>Submit
        </button>
    </div>
};

const RGBParams = ({neopixel}) => <div>
    <RGBSlider neopixel={neopixel} color='red' param='r'/>
    <RGBSlider neopixel={neopixel} color='green' param='g'/>
    <RGBSlider neopixel={neopixel} color='blue' param='b'/>
</div>;

const sliderCaptionStyle = {
    marginRight: 10,
    fontSize: 30
};

const RGBSlider = ({neopixel, color, param}) => <ParamSlider component={neopixel} param={param} style={{marginBottom: 30}}>
    <div style={{width: 30, height: 30, borderRadius: 18, backgroundColor: color, marginRight: 10}}/>
</ParamSlider>;

const RainbowParams = ({neopixel}) => <div>
    <ParamSlider component={neopixel} param={'speed'} min={-1}>
        <i className={"glyphicon glyphicon-flash"} style={sliderCaptionStyle}/>
    </ParamSlider>
</div>;

export default Neopixel