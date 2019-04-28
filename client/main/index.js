import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter as Router, Route } from "react-router-dom";

import Main from "./components/Main";
import Debug from "./debug/Debug";

const App = () => <Router>
        <Route path={"/"} exact component={Main}/>
    <Route path={"/debug"} component={Debug}/>
    </Router>
;

ReactDOM.render(<App/>, document.getElementById('app'));
