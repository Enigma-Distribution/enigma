<template>
  <div>
    <b-navbar>
      <template #brand>
        <b-navbar-item tag="router-link" :to="{ path: '/' }">
          <img
            src="https://user-images.githubusercontent.com/39585600/147443810-7a847423-7980-4d80-9779-ce23c62eeb6d.png"
            alt="Enigma Logo"
          />
        </b-navbar-item>
      </template>
      <template #start>
        <b-navbar-item tag="router-link" :to="{ path: '/tasks/all' }">
          📥&nbsp;&nbsp;Computations
        </b-navbar-item>
        <b-navbar-item tag="router-link" :to="{ path: '/transactions' }">
          💰&nbsp;&nbsp;Transactions
        </b-navbar-item>
        <b-navbar-item tag="router-link" :to="{ path: '/settings' }">
          ⚙️&nbsp;&nbsp;Settings
        </b-navbar-item>
      </template>

      <template #end>
        <b-navbar-item tag="div">
          <div class="buttons" v-if="!isLoggedIn">
            <nuxt-link :to="'/register'" class="button is-primary">
              <strong>Sign up</strong>
            </nuxt-link>
            <nuxt-link :to="'/login'" class="button is-light">
              Log in
            </nuxt-link>
          </div>
          <div class="buttons" v-else>
            <button v-on:click.prevent="logout" class="button is-light">
              Logout
            </button>
          </div>
        </b-navbar-item>
      </template>
    </b-navbar>
    <nuxt />
  </div>
</template>

<script>
import { spinupNewContainer, runPreprocessSetup, getAllTasks } from '../../main/docker'
import workerData from '../functions/workerData'

export default {
  name: "DefaultLayout",
  computed: {
    isLoggedIn() {
      return this.$store.state.isLoggedIn;
    },
  },
  methods: {
    logout() {
      this.$store.dispatch("logout");
      this.$router.push("/login");
    },

    async getworkerData() {
      const allTasks = await getAllTasks();
      const totalTasks = allTasks?.length;
      if(totalTasks && totalTasks > 5) return;
        console.log("calling worker data")
        const [response, data] = await workerData(this);
        console.log(response)
        console.log(data)
        if(response){
          console.log("returning data")
          return data
        }
    },

    async checkAgain() {
        
        const data = await this.getworkerData();
        
        let phase;
        let step;
        console.log(data)
        if(data.AVAILABLE) {
          const containerId = await spinupNewContainer();
          const token = this.$store.state.token
          const zip_url = `https://ipfs.infura.io/ipfs/${data.STEP[0].zip_file_id}`
          console.log("zip url", zip_url)
          const fileAccessLink = `https://ipfs.infura.io/ipfs/${data.STEP[0].datasource_id}`
          // console.log("fileAccessLink", fileAccessLink)
          phase = data.STEP[0].phase;
          step = data.STEP[0].step_id;
          let res = await runPreprocessSetup(containerId, zip_url, fileAccessLink, phase, step, token);
          console.log(res)
        }
    }
  },
  async mounted() {
      setInterval(this.checkAgain, 50000)
  }
};
</script>

<style>
body {
  margin: 0 !important;
}
</style>
