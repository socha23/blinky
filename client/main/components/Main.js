import React from 'react'
import LedBox from "./LedBox";

const Main = ({machine}) => <div className={"container"} style={{marginTop: 30}}>
    <div className={"row"}>
    {machine.leds.map((led, idx) =>
            <LedBox key={idx} led={led}/>)}
    </div>
</div>

export default Main