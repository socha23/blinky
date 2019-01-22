import React from 'react'
import ReactBootstrapSlider from 'react-bootstrap-slider';
import {useLed} from "../elements/ledHooks";

const SettingButton = ({className, children, onClick, active}) => <button
    style={{marginRight: 6}}
    onClick={onClick}
    className={"btn " + className + (active ? " active" : "")}
>
    {children}
</button>;


const LedBox = ({idx}) => {
    const led = useLed(idx);

    return <div className={"col-sm-4"}>

        <div className="panel panel-default">
            <div className="panel-heading">
                <h3 className="panel-title">{led.name()}</h3>
            </div>
            <div className="panel-body">
                <div style={{marginBottom: 5}}>
                    <ReactBootstrapSlider
                        value={led.value()}
                        change={e => {led.setValue(e.target.value)}}
                        step={0.01}
                        max={1}
                        min={0}
                    />
                </div>
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