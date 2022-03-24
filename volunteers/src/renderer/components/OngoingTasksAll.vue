<template>
  <div class="card" v-if="tasks != null" >
    <div class="card-content">
        <div class="media">
            <div class="media-left">
                <figure class="image is-48x48">
                    <img src="https://www.todosperte.com/gif_animate/caricamento2.gif" alt="Loader">
                </figure>
            </div>
            <div class="media-content">
                <p class="title is-4" style="color: aqua;"> {{tasks.length}} Computations</p>
                <p class="subtitle is-6" style="color: aqua;">Ongoing</p>
            </div>
        </div>
    </div>
    </div>
</template>

<script>
import { getAllTasks } from "../../main/docker";
export default {
  data() {
    return {
      tasks: null,
    };
  },
  methods: {
    async refreshStatus() {
      this.tasks = await getAllTasks();
    },
  },
  async mounted() {
    setInterval(this.refreshStatus, 2000);
  },
};
</script>

<style>
.important {
    background-color: black;
    color: aqua;
}
</style>