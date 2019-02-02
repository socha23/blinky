import React from 'react'
import {useNeopixels} from "../elements/neopixelsHooks";

const SettingButton = ({className, children, onClick, active}) => <button
    style={{marginRight: 6}}
    onClick={onClick}
    className={"btn " + className + (active ? " active" : "")}>
    {children}
</button>;


const NeopixelsBox = ({idx}) => {
    const neopixels = useNeopixels(idx);

    return <div className={"col-sm-4"}>

        <div className="panel panel-default">
            <div className="panel-heading">
                <h3 className="panel-title">{neopixels.name()}</h3>
            </div>

            <div className="panel-body">
                <div>
                    <SettingButton active={neopixels.setting() === "on"} className={"btn-primary"} onClick={neopixels.on}>On</SettingButton>
                    <SettingButton active={neopixels.setting() === "off"} className={"btn-danger"} onClick={neopixels.off}>Off</SettingButton>
                </div>
            </div>
        </div>
    </div>
};

export default NeopixelsBox