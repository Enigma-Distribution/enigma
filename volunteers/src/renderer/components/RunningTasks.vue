<template>
  <div v-if="tasks!=null">
        <section class="hero is-info">
            <div class="hero-body">
                <p class="title is-4">
                🚀&nbsp;Running Computations
                </p>
                <p class="subtitle">
                {{ tasks.length}} computations running right now.
                </p>
            </div>
        </section>
    <div class="card paddingify-small">
        <div class="card-content" v-for="task in tasks" v-bind:key="task.name">
            <div class="media">
            <div class="media-left">
                <figure class="image is-48x48">
                <img src="https://acegif.com/wp-content/uploads/loading-36.gif" alt="Loader">
                </figure>
            </div>
            <div class="media-content">
                <p class="title is-4">{{task.name}}</p>
                <p class="subtitle is-6">Running from {{task.status}}.</p>
            </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import { getAllTasks } from '../../main/docker'
export default {
    data() {
        return {
            tasks : null
        }
    },
    methods: {
        async refreshStatus() {
            this.tasks = await getAllTasks();
        }
    },
 async mounted(){
    setInterval(this.refreshStatus, 2000)
    }
}
</script>

<style>

</style>