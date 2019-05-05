import React from 'react'
import ReactDOM from 'react-dom'
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";

import Main from "./components/Main";
import Debug from "./debug/Debug";

const App = () => <Router>
    <Switch>
        <Route path={"/debug"} component={Debug}/>
        <Route path={"/"} component={Main}/>
    </Switch>
    </Router>
;

ReactDOM.render(<App/>, document.getElementById('app'));
