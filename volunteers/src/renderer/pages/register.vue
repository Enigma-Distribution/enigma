<template>
  <section
    style="
       {
        'padding':5pxs ;
      }
    "
  >
    <div class="field">
      <label class="label">Username</label>
      <div class="control">
        <input
          class="input"
          type="text"
          placeholder="Name"
          v-model="Username"
        />
      </div>
    </div>
    <div class="field">
      <label class="label">Email</label>
      <div class="control">
        <input
          class="input"
          type="email"
          placeholder="Emails"
          v-model="Email"
        />
      </div>
    </div>

    <div class="field">
      <label class="label">Password</label>
      <div class="control">
        <input
          class="input"
          type="password"
          placeholder="Password"
          v-model="Password"
        />
      </div>
    </div>
    <div class="field">
      <label class="label">UPI_id</label>
      <div class="control">
        <input
          class="input"
          type="text"
          placeholder="upi_id"
          v-model="Upi_id"
        />
      </div>
    </div>
    <div class="dropdown" v-bind:class="isActive && 'is-active'">
      <div class="dropdown-trigger">
        <button @click="dropdownActivate"
          class="button"
          aria-haspopup="true"
          aria-controls="dropdown-menu"
        >
          <span>User Type</span>
          <span class="icon is-small">
            <i class="fas fa-angle-down" aria-hidden="true"></i>
          </span>
        </button>
      </div>
      <div class="dropdown-menu" id="dropdown-menu" role="menu">
        <div class="dropdown-content">
          <button class="dropdown-item" @click="UserType = 'worker'; dropdownActivate()"> Worker </button>
          <button class="dropdown-item" @click="UserType = 'user'; dropdownActivate()"> User </button>
        </div>
      </div>
    </div>
    <div class="field">
      <div class="control">
        <button class="button is-success" v-on:click="authenticate">
          Sign Up
        </button>
      </div>
    </div>
    <div class="field">
      <div class="control">
        <nuxt-link class="button" :to="'/login'">Login</nuxt-link>
      </div>
    </div>
  </section>
</template>
<script>
import register from "../functions/register";
export default {
  data() {
    return {
      Username: "",
      Email: "",
      Password: "",
      isActive: false,
      Upi_id: ""
    };
  },

  methods: {
    async authenticate() {
      console.log(this);
      const [status, data] = await register(
        this.Email,
        this.Password,
        this.Username,
        this.UserType,
        this.Upi_id,
        this
      );
      if (status) {
        this.$router.push("/")
      }
    },
    async dropdownActivate() {
        this.isActive = !this.isActive
    }
  },
};
</script>

<style>
</style>