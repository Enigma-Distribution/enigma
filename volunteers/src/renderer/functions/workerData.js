import baseURL from "./baseURL";
import axios from "axios";

export default async function (context) {
    const token = context.$store.state.token;
    //context.$axios.setHeader('Content-Type', 'application/json')
    const response = await axios.post(
        `${baseURL}/worker/allot-me`,
        {},
        {
            headers: {'Content-Type' : 'application/json', 'token': token}
        }
    );

    if (response.STATUS == "OK") {
        return [true, response.STEP]
    }
    else if (response.STATUS == "FAIL") {
        return [false, response.MSG]
    }
    return [false, "Problem with API call. Contact Developers."]
}