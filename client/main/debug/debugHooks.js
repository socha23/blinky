import React, {useEffect, useState} from 'react'
import fetch from "isomorphic-fetch";

export const useDebug = () => {
    const [state, setState] = useState({components: []});
    useEffect(() => {
        const handler = setInterval(() => {
            fetch("/state")
                .then(r => r.json())
                .then(state => {setState(state)});
            }, 50);
        return () => {
            clearInterval(handler)
        }
    }, []);
    return state;
};
