import React from 'react'
import {EnumParamRadio, EnumParamRadioRow, ParamSlider, SettingsSection, SliderIcon} from "./elements";

export const TurnOnEffectSection = ({component}) => <SettingsSection caption={'Turn on effect:'}>
    <EnumParamRadioRow>
        <EnumParamRadio param={'turn_on_effect'} value={'none'} component={component}>
            None
        </EnumParamRadio>
        <EnumParamRadio param={'turn_on_effect'} value={'fade_in'} component={component}>
            Fade in
        </EnumParamRadio>
        <EnumParamRadio param={'turn_on_effect'} value={'neon_flicker'} component={component}>
            Neon flicker
        </EnumParamRadio>
    </EnumParamRadioRow>
    <TurnOnParams component={component}/>
</SettingsSection>;


const TurnOnParams = ({component}) => {
    switch (component.params.turn_on_effect) {
        case "fade_in":
            return <div>
                <ParamSlider component={component} param={"fade_in_duration"}>
                    <SliderIcon className={'glyphicon glyphicon-time'}/>
                </ParamSlider>
            </div>;
        case "neon_flicker":
            return <div>
                <ParamSlider component={component} param={"neon_flicker_turn_on_speed"}>
                    <SliderIcon className={'glyphicon glyphicon-time'}/>
                </ParamSlider>
            </div>;
        default:
            return <div/>
    }
};

export const TurnOffEffectSection = ({component}) => <SettingsSection caption={'Turn off effect:'}>
    <EnumParamRadioRow>
        <EnumParamRadio param={'turn_off_effect'} value={'none'} component={component}>
            None
        </EnumParamRadio>
        <EnumParamRadio param={'turn_off_effect'} value={'fade_out'} component={component}>
            Fade out
        </EnumParamRadio>
    </EnumParamRadioRow>
    <TurnOffParams component={component}/>
</SettingsSection>;


const TurnOffParams = ({component}) => {
    switch (component.params.turn_off_effect) {
        case "fade_out":
            return <div>
                <ParamSlider component={component} param={"fade_out_duration"}>
                    <SliderIcon className={'glyphicon glyphicon-time'}/>
                </ParamSlider>
            </div>;
        default:
            return <div/>
    }
};

export const AdditionalEffectSection = ({component}) => <SettingsSection caption={'Additional effect:'}>
    <EnumParamRadioRow>
        <EnumParamRadio param={'additional_effect'} value={'none'} component={component}>
            None
        </EnumParamRadio>
        <EnumParamRadio param={'additional_effect'} value={'neon_flicker'} component={component}>
            Neon flicker
        </EnumParamRadio>
        <EnumParamRadio param={'additional_effect'} value={'pulse'} component={component}>
            Pulse
        </EnumParamRadio>
    </EnumParamRadioRow>
    <AdditionalEffectParams component={component}/>
</SettingsSection>;


const AdditionalEffectParams = ({component}) => {
    switch (component.params.additional_effect) {
        case "neon_flicker":
            return <div>
                <ParamSlider component={component} param={"neon_flicker_intensity"}>
                    <SliderIcon className={'glyphicon glyphicon-flash'}/>
                </ParamSlider>
            </div>;
        case "pulse":
            return <div>
                <ParamSlider component={component} param={"pulse_duration"}>
                    <SliderIcon className={'glyphicon glyphicon-time'}/>
                </ParamSlider>
                <ParamSlider component={component} param={"pulse_intensity"}>
                    <SliderIcon className={'glyphicon glyphicon-flash'}/>
                </ParamSlider>
            </div>;
        default:
            return <div/>
    }
};

export const EffectSections = ({component}) => [
    <TurnOnEffectSection key={"on"} component={component}/>,
    <TurnOffEffectSection key={"off"} component={component}/>,
    <AdditionalEffectSection key={"additional"} component={component}/>
];