<template>
  <section style="{ 'padding' : 5pxs }">
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

        <!-- <div class="field">
        <label class="label">User Type</label>
        <div class="control">
            <input class="input" type="text" placeholder="Type" v-model="UserType">
        </div>
        </div> -->

        <div class="field">
        <div class="control">
            <button class="button is-success" v-on:click="authenticate">Login</button>
        </div>
        </div>
        <div class="field">
        <div class="control">
            <nuxt-link class="button" :to="'/register'">Sign Up</nuxt-link>
        </div>
        </div>

  </section>
</template>

<script>
import login from '../functions/login'
export default {
    data() {
     return {
        Email : "",
        Password : "",
        UserType: "worker"
     }
    },

    methods: {
        async authenticate(){
           const [status, data] =  await login(this.Email, this.Password, this.UserType,this);
           if(status){
               this.$router.push('/')
           }
        }
    }
}
</script>

<style>

</style>