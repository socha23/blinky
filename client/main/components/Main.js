import React from 'react'
import {useMachineModel} from "../elements/componentHooks"
import {Neopixel, NeopixelSettings} from "./Neopixel";
import {Led, LedSettings} from "./Led";
import {Link, Route, Switch} from "react-router-dom";

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
    return <div>
        <SettingsHeader component={component}/>
        {settings}
    </div>;
};

const SettingsHeader = ({component}) => <Link to={'/'}>
        <div style={{
            backgroundColor: "rgb(58, 63, 68)",
            fontSize: 30,
            display: "flex",
            alignItems: "center",
            color: "#ccc",
            cursor: "pointer",
            height: 60,

        }}>
            <i style={{marginLeft: 10, marginRight: 5}} className={"glyphicon glyphicon-chevron-left"}/>
            <h2 style={{margin: 10}}>{component.name}</h2>
        </div>
</Link>;

export default Routing