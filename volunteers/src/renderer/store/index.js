export const state = () => {
    const tokenNew = localStorage.getItem("token")
    var isLoggedIn = false;
    if(tokenNew) isLoggedIn = true;
    return {
        isLoggedIn: isLoggedIn,
        token: tokenNew
    }
}

export const mutations = {
    SET_TOKEN(state, token){
        state.token = token
        state.isLoggedIn = true
    },
    REM_TOKEN(state){
        state.token = undefined
        state.isLoggedIn = false
    }
}

export const actions = {
    setToken(context, token){
        localStorage.setItem("token", token)
        context.commit('SET_TOKEN', token)
    },
    logout(context){
        localStorage.removeItem("token")
        context.commit('REM_TOKEN')
    }
}