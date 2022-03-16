import baseURL from "./baseURL";

export default async function (context) {
    context.$axios.setHeader('Content-Type', 'application/json')
    const response = await context.$axios.$post(
        `${baseURL}/worker/allot-me`,
        {}
    );

    if (response.STATUS == "OK") {
        return [response, undefined]
    }
    else if (response.STATUS == "FAIL") {
        return [false, response.MSG]
    }
    return [false, "Problem with API call. Contact Developers."]
}