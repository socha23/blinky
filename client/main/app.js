import React from 'react'
import LedBox from "./components/ledBox";

const App = () => <div>
    <LedBox pin={24} title={"Czerwony"}/>
    <LedBox pin={25} title={"Biały"}/>
</div>

export default App