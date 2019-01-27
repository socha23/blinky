import React from 'react'
import {useFire} from "../elements/fireHooks";
import ReactBootstrapSlider from "react-bootstrap-slider";

const SettingButton = ({className, children, onClick, active}) => <button
    style={{marginRight: 6}}
    onClick={onClick}
    className={"btn " + className + (active ? " active" : "")}>
    {children}
</button>;


const FireBox = ({idx}) => {
    const fire = useFire(idx);

    return <div className={"col-sm-4"}>

        <div className="panel panel-default">
            <div className="panel-heading">
                <h3 className="panel-title">{fire.name()}</h3>
            </div>

            <div className="panel-body">
                <div style={{marginBottom: 5}}>
                    <ReactBootstrapSlider
                        value={fire.intensity()}
                        change={e => {fire.setIntensity(e.target.value)}}
                        step={0.01}
                        max={1}
                        min={0}
                    />
                </div>
                <div>
                    <SettingButton active={fire.setting() === "on"} className={"btn-primary"} onClick={fire.on}>On</SettingButton>
                    <SettingButton active={fire.setting() === "off"} className={"btn-danger"} onClick={fire.off}>Off</SettingButton>
                </div>
            </div>
        </div>
    </div>
};

export default FireBox