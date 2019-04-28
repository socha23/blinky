import React from 'react'
import ReactBootstrapSlider from "react-bootstrap-slider";


const toggleButtonStyle = {
    fontSize: 40,
    padding: 15,
    flexGrow: 1,
    border: "none",
    backgroundColor: "black",
    cursor: "pointer",
    textAlign: "center"
};

export const OnOffToggle = ({component}) => {
    function toggle() {
        if (component.on) {
            component.turnOff()
        } else {
            component.turnOn()
        }
    }

    return <div style={{...toggleButtonStyle, color: component.on ? "yellow" : "#888"}} onClick={toggle}>
        <i className={"glyphicon glyphicon-certificate"}/>
    </div>
};

export const SettingsToggle = ({settingsDisplayed, toggleSettingsDisplayed}) => {

    return <div style={{...toggleButtonStyle, color: settingsDisplayed ? "white" : "#888"}} onClick={e => toggleSettingsDisplayed(!settingsDisplayed)}>
        <i className={"glyphicon glyphicon-cog"}/>
    </div>
};

export const SettingButton = ({icon, component, setting}) => {
    const style = {
        fontSize: 40,
        flexGrow: 1,
        color: "#888",
        backgroundColor: "black",
        cursor: "pointer",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
    };

    const iconStyle = {
        padding: 10,
        border: "3px solid black",
        borderColor: "black",
        borderRadius: 5,
    };

    if (component.setting === setting) {
        iconStyle.borderColor = "white";
        iconStyle.color = "white";
    }

    return <div
        style={style}
        onClick={() => {
            component.setSetting(setting)
        }}>
        <i style={iconStyle} className={icon}/>
    </div>
};


const sliderContainerStyle = {
    display: "flex",
    alignItems: "center",
    marginBottom: 5,
};

export const ParamSlider = ({component, param, children, min = 0, style = {}}) =>
    <div style={{...sliderContainerStyle, marginBottom: 15, marginTop: 15, ...style}}>
        {children}
        <div style={{flexGrow: 1}}>
            <Slider
                value={component.params[param]}
                onChange={v => {
                    component.setParam(param, v)
                }}
                onStop={v => {
                    component.updateParam(param, v)
                }}
                on
                min={min}
            />
        </div>
    </div>;


const Slider = ({value, onChange, onStop, min = 0}) => <ReactBootstrapSlider
    value={value}
    change={e => {
        onChange(e.target.value)
    }}
    slideStop={e => {
        onStop(e.target.value)
    }}
    step={0.01}
    min={min}
    max={1}
/>;
