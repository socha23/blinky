import React from 'react'
import {BrightnessSlider, ComponentBox, EnumParamRadio, EnumParamRadioRow, SettingButton, SettingsSection} from "./elements";

export const Led = ({component, renderSettingsLink}) => <ComponentBox component={component} renderSettingsLink={renderSettingsLink}/>

export const LedSettings = ({led}) => <div>
    <SettingsSection caption={'Brightness:'}>
        <BrightnessSlider component={led}/>
    </SettingsSection>
    <SettingsSection caption={'Setting:'}>
        <div style={{marginTop: 10, marginBottom: 20, display: "flex", justifyContent: "space-between"}}>
            <SettingButton component={led} setting='const' icon={"glyphicon glyphicon-star"}/>
            <SettingButton component={led} setting='blink' icon={"glyphicon glyphicon-adjust"}/>
            <SettingButton component={led} setting='pulse' icon={"glyphicon glyphicon-glass"}/>
        </div>
    </SettingsSection>
    <SettingsSection caption={'Turn on effect:'}>
        <EnumParamRadioRow>
            <EnumParamRadio param={'turn_on_effect'} value={'none'} component={led}>
                None
            </EnumParamRadio>
            <EnumParamRadio param={'turn_on_effect'} value={'fade_in'} component={led}>
                Fade in
            </EnumParamRadio>
        </EnumParamRadioRow>
    </SettingsSection>
</div>;

