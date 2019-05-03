import React from 'react'
import useMachineModel from "../elements/componentHooks"
import Neopixel from "./Neopixel";
import Led from "./Led";
import {Link, Route, Switch} from "react-router-dom";

const Routing = () => {
    const model = useMachineModel();
    return <Switch>
        <Route path={'/settings/:id'} render={({match}) => {
            const id = match.params.id;
            return <ComponentSettings component={model.componentsById[id]} type={model.componentTypes[id]}/>
        }}/>
        <Route path={'/'} render={() => <ComponentList model={model}/>}/>
    </Switch>
};

const ComponentList = ({model}) =>
    <div>
        {model.leds.map(led =>
            <Led key={led.id}
                 component={led}
                 renderSettingsLink={children => <Link to={'/settings/' + led.id}>{children}</Link>}
            />)}
        {model.neopixels.map(px =>
            <Neopixel key={px.id}
                      component={px}
                      renderSettingsLink={children => <Link to={'/settings/' + px.id}>{children}</Link>}
            />)}
    </div>;



const ComponentSettings = ({component, componentType}) => <div>
    <Link to={'/'}>Back to list</Link>
    <div>Settings for {componentType} named {component.name}</div>
</div>;

export default Routing