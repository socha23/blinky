import React from 'react'
import {useNeopixel} from "../elements/neopixelsHooks";
import ReactBootstrapSlider from "react-bootstrap-slider";

const SettingButton = ({className, children, onClick, active}) => <button
    style={{marginRight: 6}}
    onClick={onClick}
    className={"btn " + className + (active ? " active" : "")}>
    {children}
</button>;


const NeopixelBox = ({idx}) => {
    const neopixel = useNeopixel(idx);

    return <div className={"col-sm-4"}>

        <div className="panel panel-default">
            <div className="panel-heading">
                <h3 className="panel-title">{neopixel.name()}</h3>
            </div>

            <div className="panel-body">
                <div style={{marginBottom: 5}}>
                    <ReactBootstrapSlider
                        value={neopixel.brightness()}
                        change={e => {neopixel.setBrightness(e.target.value)}}
                        step={0.01}
                        max={1}
                        min={0}
                    />
                </div>

                <div>
                    <SettingButton active={neopixel.setting() === "on"} className={"btn-primary"} onClick={neopixel.on}>On</SettingButton>
                    <SettingButton active={neopixel.setting() === "fire"} className={"btn-info"} onClick={neopixel.fire}>Fire</SettingButton>
                    <SettingButton active={neopixel.setting() === "off"} className={"btn-danger"} onClick={neopixel.off}>Off</SettingButton>
                </div>
            </div>
        </div>
    </div>
};

export default NeopixelBox