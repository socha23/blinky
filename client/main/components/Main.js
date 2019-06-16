import React from 'react'
import {useMachineModel} from "../elements/componentHooks"
import {Neopixel, NeopixelSettings} from "./Neopixel";
import {Led, LedSettings} from "./Led";
import {Link, Route, Switch, withRouter} from "react-router-dom";
import {OnOffToggle} from "./elements";

const Routing = () => {
    const model = useMachineModel();
    return <Switch>
        <Route path={'/settings/:id'} render={({match}) => {
            const component = model.componentsById[match.params.id];
            if (!component) {
                return <div>Loading...</div>
            } else {
                return <ComponentSettings component={component}/>
            }
        }}/>
        <Route path={'/'} render={() => <ComponentList model={model}/>}/>
    </Switch>
};

const ComponentList = ({model}) =>
    <div>
        <MachineHeader machine={model.machine}/>
        {
            model.components.map(c => <ComponentListElem key={c.id} component={c}/>)
        }
    </div>;

const ComponentListElem = ({component}) => {
    const renderSettingsLink = (children, style) => <Link style={style} to={'/settings/' + component.id}>{children}</Link>;
    switch (component.type) {
        case "led":
            return <Led component={component} renderSettingsLink={renderSettingsLink}/>
        case "neopixel":
            return <Neopixel component={component} renderSettingsLink={renderSettingsLink}/>
    }
};


const ComponentSettings = ({component}) => {
    let settings = <div/>;
    switch (component.type) {
        case "led":
            settings = <LedSettings led={component}/>;
            break;
        case "neopixel":
            settings = <NeopixelSettings neopixel={component}/>;
            break;
    }
    return <div style={{position: "relative"}}>
        <SettingsHeader component={component}/>
        <div style={{marginTop: 65, zIndex: 1}}>
            {settings}
        </div>
    </div>;
};

const headerStyle = {
    backgroundColor: "rgb(58, 63, 68)",
    fontSize: 30,
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    color: "#ccc",
    cursor: "pointer",
    height: 60,
    paddingRight: 10,
    width: "100%",
    borderBottom: "1px solid #555"
};

const SettingsHeader = withRouter(({component, history}) =>
    <div style={{
        ...headerStyle,
        position: 'fixed',
        top: 0,
        zIndex: 2,
    }}>
        <div style={{display: "flex", alignItems: "center"}} onClick={() => {
            history.push("/")
        }}>
            <i style={{marginLeft: 10, marginRight: 5}} className={"glyphicon glyphicon-chevron-left"}/>
            <h2 style={{margin: 10}}>{component.name}</h2>
        </div>
        <OnOffToggle component={component}/>
    </div>);

const MachineHeader = ({machine}) =>
    <div style={headerStyle}>
        <div style={{display: "flex", alignItems: "center"}}>
            <h2 style={{margin: 10}}>{machine.name}</h2>
        </div>
        <OnOffToggle component={machine}/>
    </div>;


export default Routing