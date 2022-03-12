
export const setUser = (user) => async (dispatch) => {
    dispatch({ type: "SET_USER", payload: user });
};
