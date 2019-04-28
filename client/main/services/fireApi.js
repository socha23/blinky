import {putJson} from "./apiUtils";

export function intensity(id, intensity) {
    putJson(fireAddr(id) + "/intensity/" + intensity)
}

function fireAddr(id) {
    return "/fire/" + id
}

