
const initialState = {
  user: localStorage.getItem("USER") || null
}

export const userReducer = (state = initialState, action) => {
    switch (action.type) {
      case "SET_USER":
        return { user: action.payload };
      // case "GET_USER":
      //   return { loading: state.user };
      // case USER_REGISTER_FAIL:
      //   return { loading: false, error: action.payload };
      default:
        return state;
    }
};