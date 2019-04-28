import React, {useState} from 'react'
import {useNeopixel} from "../elements/neopixelsHooks";
import ReactBootstrapSlider from "react-bootstrap-slider";


const NeopixelBox = ({idx}) => {
    const neopixel = useNeopixel(idx);
    const [settingsDisplayed, toggleSettingsDisplayed] = useState(false);

    return <div style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        borderBottom: "1px solid #888",
    }}>
        <h2 style={{margin: 10, marginTop: 20, color: "#ccc"}}>{neopixel.name}</h2>
        <div style={{display: "flex", justifyContent: "space-around", width: "100%"}}>
            <OnOffToggle neopixel={neopixel}/>
            <SettingsToggle neopixel={neopixel} settingsDisplayed={settingsDisplayed} toggleSettingsDisplayed={toggleSettingsDisplayed}/>
        </div>
        {settingsDisplayed ? <SettingsBox neopixel={neopixel}/> : <div/>}
    </div>
};


const toggleButtonStyle = {
    fontSize: 40,
    padding: 15,
    flexGrow: 1,
    border: "none",
    backgroundColor: "black",
    cursor: "pointer",
    textAlign: "center"
};

const OnOffToggle = ({neopixel}) => {
    function toggle() {
        if (neopixel.on) {
            neopixel.turnOff()
        } else {
            neopixel.turnOn()
        }
    }

    return <div style={{...toggleButtonStyle, color: neopixel.on ? "yellow" : "#888"}} onClick={toggle}>
        <i className={"glyphicon glyphicon-certificate"}/>
    </div>
};

const SettingsToggle = ({settingsDisplayed, toggleSettingsDisplayed}) => {

    return <div style={{...toggleButtonStyle, color: settingsDisplayed ? "white" : "#888"}} onClick={e => toggleSettingsDisplayed(!settingsDisplayed)}>
        <i className={"glyphicon glyphicon-cog"}/>
    </div>
};

const SettingsBox = ({neopixel}) => <div style={{width: "100%", padding: 10, marginBottom: 10}}>
    <BrightnessSlider neopixel={neopixel}/>
    <div style={{marginTop: 30, marginBottom: 10, display: "flex", justifyContent: "space-between"}}>
        <SettingButton neopixel={neopixel} setting='rgb' icon={"glyphicon glyphicon-menu-hamburger"}/>
        <SettingButton neopixel={neopixel} setting='rainbow' icon={"glyphicon glyphicon-heart"}/>
        <SettingButton neopixel={neopixel} setting='fire' icon={"glyphicon glyphicon-fire"}/>
        <SettingButton neopixel={neopixel} setting='effect' icon={"glyphicon glyphicon-wrench"}/>
    </div>
    <SettingParams neopixel={neopixel}/>
</div>;

const SettingButton = ({icon, neopixel, setting}) => {
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

    if (neopixel.setting === setting) {
        iconStyle.borderColor = "white";
        iconStyle.color = "white";
    }

    return <div
        style={style}
        onClick={() => {
            neopixel.setSetting(setting)
        }}>
        <i style={iconStyle} className={icon}/>
    </div>
};


const sliderContainerStyle = {
    display: "flex",
    alignItems: "center",
    marginBottom: 5,
};

const sliderCaptionStyle = {
    marginRight: 10,
    fontSize: 30
};

const BrightnessSlider = ({neopixel}) => <ParamSlider neopixel={neopixel} param={"brightness"}>
    <i className={"glyphicon glyphicon-asterisk"} style={sliderCaptionStyle}/>
</ParamSlider>;

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
            onClick={e => neopixel.setParam("body", body, onSuccess, onFailure)}>Submit</button>
    </div>
};

const RGBParams = ({neopixel}) => <div>
    <RGBSlider neopixel={neopixel} color='red' param='r'/>
    <RGBSlider neopixel={neopixel} color='green' param='g'/>
    <RGBSlider neopixel={neopixel} color='blue' param='b'/>
</div>;


const RGBSlider = ({neopixel, color, param}) => <ParamSlider neopixel={neopixel} param={param} style={{marginBottom: 30}}>
    <div style={{width: 30, height: 30, borderRadius: 18, backgroundColor: color, marginRight: 10}}/>
</ParamSlider>;


const RainbowParams = ({neopixel}) => <div>
    <ParamSlider neopixel={neopixel} param={'speed'} min={-1}>
        <i className={"glyphicon glyphicon-flash"} style={sliderCaptionStyle}/>
    </ParamSlider>
</div>;


const ParamSlider = ({neopixel, param, children, min = 0, style = {}}) =>
    <div style={{...sliderContainerStyle, marginBottom: 15, marginTop: 15, ...style}}>
        {children}
        <div style={{flexGrow: 1}}>
            <Slider
                value={neopixel.params[param]}
                onChange={v => {
                    neopixel.setParam(param, v)
                }}
                min={min}
            />
        </div>
    </div>;


const Slider = ({value, onChange, min = 0}) => <ReactBootstrapSlider
        value={value}
        change={e => {
            onChange(e.target.value)
        }}
        step={0.01}
        min={min}
        max={1}
    />;

export default NeopixelBox