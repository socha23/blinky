import React from 'react'
import ReactBootstrapSlider from './FixedBootstrapSlider'

export const ComponentBox = ({component, renderSettingsLink}) => {
    return <div style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        borderBottom: "1px solid #888",
    }}>
        <h2 style={{margin: 10, marginTop: 20, color: "#ccc"}}>{component.name}</h2>
        <div style={{display: "flex", justifyContent: "space-around", width: "100%"}}>
            <OnOffToggle component={component}/>
            {
                renderSettingsLink(<div>
                    <i className={"glyphicon glyphicon-cog"}/>
                </div>, {...toggleButtonStyle, color: "#888"})
            }
        </div>
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

export const SettingsSection = ({caption="", children}) => <div style={{borderBottom: "1px solid #888", margin: 10}}>
    <div style={{fontSize: 20, color: "#ccc"}}>{caption}</div>
    <div>{children}</div>
</div>;

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


const sliderCaptionStyle = {
    marginRight: 10,
    fontSize: 30
};

export const SliderIcon = ({className}) => <i className={className} style={sliderCaptionStyle}/>;

export const BrightnessSlider = ({component}) => <ParamSlider component={component} param={"brightness"}>
    <SliderIcon className={"glyphicon glyphicon-asterisk"}/>
</ParamSlider>;

export const ParamSlider = ({component, param, children, min = 0, style = {}, caption = null}) => {
    return <div>
        {caption ? <div style={{fontSize: 20, marginBottom: -10, marginLeft: 5, color: "#ccc"}}>{caption}</div> : <div/>}
        <div style={{...sliderContainerStyle, marginBottom: 15, marginTop: 15, ...style}}>
            {children}
            <div style={{flexGrow: 1}}>
                <Slider
                    params={component.params}
                    value={component.params[param]}
                    onChange={v => {
                        component.setParam(param, v)
                    }}
                    onStop={v => {
                        component.updateParam(param, v)
                    }}
                    min={min}
                />
            </div>
        </div>
    </div>};



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

export const EnumParamRadioRow = ({children}) => <div style={{
    display: 'flex',
    justifyContent: 'flex-start',
    marginTop: 10,
    marginBottom: 10,
    marginLeft: 5,
}}>{children}</div>;

export const EnumParamRadio = ({component, param, value, children}) => {
    const checked = component.params[param] == value;
    return <div
        style={{
            display: 'flex',
            alignItems: 'center',
            fontSize: 20,
            color: checked ? 'white' : '#888',
            marginRight: 20,
        }}
        onClick={_ => {console.log(param, value); component.updateParam(param, value)}}
    >
        <i style={{marginRight: 5}} className={'glyphicon ' + (checked ? 'glyphicon-check' : 'glyphicon-unchecked')}/>
        {children}
    </div>
};