import React from 'react'
import makeLed from '../services/led'

const LedBox = ({pin, title}) => {
    const led = makeLed(pin);
    return <div>
        <h1>{title}</h1>
        <a onClick={led.on}>ON</a>
        <a onClick={led.off}>OFF</a>
    </div>
};

export default LedBox