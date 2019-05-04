import React from 'react'
import {BrightnessSlider, ComponentBox, ParamSlider, SettingButton, SettingsSection} from "./elements";

export const Neopixel = ({component, renderSettingsLink}) => <ComponentBox component={component} renderSettingsLink={renderSettingsLink}/>

export const NeopixelSettings = ({neopixel}) => <div>
    <SettingsSection caption={'Brightness:'}>
        <BrightnessSlider component={neopixel}/>
    </SettingsSection>
    <SettingsSection caption={'Setting:'}>
        <div style={{marginTop: 10, marginBottom: 10, display: "flex", justifyContent: "space-between"}}>
            <SettingButton component={neopixel} setting='rgb' icon={"glyphicon glyphicon-menu-hamburger"}/>
            <SettingButton component={neopixel} setting='rainbow' icon={"glyphicon glyphicon-heart"}/>
            <SettingButton component={neopixel} setting='fire' icon={"glyphicon glyphicon-fire"}/>
        </div>
        <SettingParams neopixel={neopixel}/>
    </SettingsSection>
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

const RGBSlider = ({neopixel, color, param}) => <ParamSlider component={neopixel} param={param} style={{marginBottom: 30}}>
    <div style={{width: 30, height: 30, borderRadius: 18, backgroundColor: color, marginRight: 10}}/>
</ParamSlider>;

const RainbowParams = ({neopixel}) => <div>
    <ParamSlider caption="Speed:" component={neopixel} param={'speed'}/>
</div>;

const FireParams = ({neopixel}) => <div>
    <ParamSlider caption="Intensity:" component={neopixel} param={'intensity'}/>
</div>;
