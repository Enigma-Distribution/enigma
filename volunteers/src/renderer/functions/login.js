import baseURL from "./baseURL.js";
import axios from "axios";

export default async function(email, password, context) {
    //return [true, undefined]
    //context.$axios.setHeader('Content-Type', 'application/json')
    const response = await axios.post(
        `${baseURL}/authenticate/user`,
        {
            email: email,
            password: password
        },
        {
            headers: {'Content-Type' : 'application/json'}
        }
    );
    if (response.STATUS == "OK") {
        context.$store.dispatch('setToken', response.TOKEN)
        return [true, undefined]
    }
    else if (response.STATUS == "FAIL") {
        return [false, response.MSG]
    }
    return [false, "Problem with API call. Contact Developers."]
}