import baseURL from "./baseURL";
import axios from "axios";

export default async function(email, password, name, context) {
    //return [true, undefined]
    
    //context.$axios.setHeader('Content-Type', 'application/json')
    const response = await axios.post(
        `${baseURL}/authenticate/user/new`,
        {
            email: email,   
            password: password,
            username: name
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