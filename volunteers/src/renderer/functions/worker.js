import baseURL from "./baseURL";
import axios from "axios";

export default function (phase, step_id, hash, context) {
    const response = await axios.post(
        `${baseURL}/worker/submit-result`,
        {
            step_id: step_id,
            phase: phase,
            result_file_id: hash
        },
        {
            headers: { 'Content-Type': 'application/json' }
        }
    );
    if (response.STATUS == "OK") {
        return [true, undefined]
    }
    else if (response.STATUS == "FAIL") {
        return [false, response.MSG]
    }
    return [false, "Problem with API call. Contact Developers."]
}