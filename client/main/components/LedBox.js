import React from 'react'

const SettingButton = ({className, children, onClick, active}) => <button
    style={{marginRight: 6}}
    onClick={onClick}
    className={"btn " + className + (active ? " active" : "")}
>
    {children}
</button>;


const LedBox = ({led}) => {
    return <div className={"col-sm-4"}>

        <div className="card">
            <div className="card-body">
                <h5 className="card-title">{led.name()}</h5>
                <SettingButton active={led.setting() === "on"} className={"btn-primary"} onClick={led.on}>On</SettingButton>
                <SettingButton active={led.setting() === "blink"} className={"btn-secondary"} onClick={led.blink}>Blink</SettingButton>
                <SettingButton active={led.setting() === "pulse"} className={"btn-secondary"} onClick={led.pulse}>Pulse</SettingButton>
                <SettingButton active={led.setting() === "off"} className={"btn-danger"} onClick={led.off}>Off</SettingButton>
            </div>
        </div>

    </div>
};

export default LedBox