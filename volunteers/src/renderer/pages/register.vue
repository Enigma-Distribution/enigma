<template>
  <section style="{ 'padding' : 5pxs }">
      <div class="field">
        <label class="label">Username</label>
        <div class="control">
            <input class="input" type="text" placeholder="Name" v-model="Username">
        </div>
        </div>
      <div class="field">
        <label class="label">Email</label>
        <div class="control">
            <input class="input" type="email" placeholder="Emails" v-model="Email">
        </div>
        </div>

        <div class="field">
        <label class="label">Password</label>
        <div class="control">
            <input class="input" type="password" placeholder="Password" v-model="Password">
        </div>
        </div>
        <div class="field">
        <div class="control">
            <button class="button is-success" v-on:click="authenticate">Sign Up</button>
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
import register from '../functions/register'
export default {
    data() {
        return {
            Username : "",
            Email : "",
            Password : ""
        }

    },

    methods : {
        async authenticate() {
            console.log(this)
            const [status, data ] = await register(this.Email, this.Password, this.Username, this)
            if(status){
                this.$router.push('/')
            }
        }
    }
}
</script>

<style>

</style>