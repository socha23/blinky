import React from 'react'
import ReactBootstrapSlider from 'react-bootstrap-slider';

const SettingButton = ({className, children, onClick, active}) => <button
    style={{marginRight: 6}}
    onClick={onClick}
    className={"btn " + className + (active ? " active" : "")}
>
    {children}
</button>;


const LedBox = ({led}) => {
    return <div className={"col-sm-4"}>

        <div className="panel panel-default">
            <div className="panel-heading">
                <h3 className="panel-title">{led.name()}</h3>
            </div>
            <div className="panel-body">
                <ReactBootstrapSlider
                    value={50}
                    step={1}
                    max={100}
                    min={0}
                />
                <div>
                    <SettingButton active={led.setting() === "on"} className={"btn-primary"} onClick={led.on}>On</SettingButton>
                    <SettingButton active={led.setting() === "blink"} className={"btn-info"} onClick={led.blink}>Blink</SettingButton>
                    <SettingButton active={led.setting() === "pulse"} className={"btn-info"} onClick={led.pulse}>Pulse</SettingButton>
                    <SettingButton active={led.setting() === "off"} className={"btn-danger"} onClick={led.off}>Off</SettingButton>
                </div>
            </div>
        </div>
    </div>
};

export default LedBox