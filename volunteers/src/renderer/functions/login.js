import baseURL from "./baseURL.js";
import axios from "axios";

export default async function(email, password, user_type, context) {
    //return [true, undefined]
    //context.$axios.setHeader('Content-Type', 'application/json')
    const response = await axios.post(
        `${baseURL}/authenticate/user`,
        {
            email: email,
            password: password,
            user_type: user_type
        },
        {
            headers: {'Content-Type' : 'application/json'}
        }
    );
    console.log(response)
    if (response.data.STATUS == "OK") {
        context.$store.dispatch('setToken', response.data.TOKEN)
        return [true, undefined]
    }
    else if (response.data.STATUS == "FAIL") {
        return [false, response.MSG]
    }
    return [false, "Problem with API call. Contact Developers."]
}