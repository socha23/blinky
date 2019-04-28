import React from 'react'
import {BrightnessSlider, ComponentBox, SettingButton} from "./elements";
import {useLed} from "../elements/ledHooks";

const Led = ({idx}) => {
    const led = useLed(idx);
    return <ComponentBox component={led}>
        <SettingsBox led={led}/>
    </ComponentBox>
};

const SettingsBox = ({led}) => <div style={{width: "100%", padding: 10, marginBottom: 10}}>
    <BrightnessSlider component={led}/>
    <div style={{marginTop: 30, marginBottom: 10, display: "flex", justifyContent: "space-between"}}>
        <SettingButton component={led} setting='const' icon={"glyphicon glyphicon-star"}/>
        <SettingButton component={led} setting='blink' icon={"glyphicon glyphicon-adjust"}/>
        <SettingButton component={led} setting='pulse' icon={"glyphicon glyphicon-glass"}/>
    </div>
</div>;


export default Led