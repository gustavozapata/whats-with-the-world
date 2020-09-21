<template>
  <div>
    <img id="logo" alt="Vue logo" src="./assets/logo.jpg" />
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <Intro message="What's With The World" />
  </div>
</template>

<script>
// import HelloWorld from "./components/HelloWorld.vue";
import Intro from "./components/Intro.vue";

export default {
  name: "App",
  components: {
    // HelloWorld
    Intro,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
#logo {
  width: 180px;
}
</style>
