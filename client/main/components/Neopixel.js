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
    </div>
    <SettingParams neopixel={neopixel}/>
</div>;

const SettingParams = ({neopixel}) => {
    switch (neopixel.setting) {
        case "rgb":
            return <RGBParams neopixel={neopixel}/>;
        case "rainbow":
            return <RainbowParams neopixel={neopixel}/>;
        case "fire":
            return <FireParams neopixel={neopixel}/>;
        default:
            return <div/>
    }
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
    <ParamSlider component={neopixel} param={'speed'} min={0}>
        <i className={"glyphicon glyphicon-flash"} style={sliderCaptionStyle}/>
    </ParamSlider>
</div>;

const FireParams = ({neopixel}) => <div>
    <ParamSlider component={neopixel} param={'intensity'}>
        <i className={"glyphicon glyphicon-fire"} style={sliderCaptionStyle}/>
    </ParamSlider>
</div>;



    export default Neopixel