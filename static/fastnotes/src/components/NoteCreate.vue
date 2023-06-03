<script setup>
import NavBar from "./NavBar.vue"
import {useNoteStore} from "../stores/note";
import {ref} from "vue";

const notesStore = useNoteStore();

const noteIn = ref({})
</script>

<template>
<NavBar></NavBar>

    <h1>Notiz erstellen</h1>

    <div id="input">
        <span>Titel eingeben</span>
        <b-form-input v-model="noteIn.title" type="text" placeholder="Titel eingeben" size="lg"></b-form-input>
        <span>Notiz eingeben</span>
        <b-textarea v-model="noteIn.text" type="text" placeholder="Notiz eingeben" size="lg" rows="6"></b-textarea>
        <div id="Button">
            <b-button @click="notesStore.create(noteIn)" variant="primary">Notiz speichern</b-button>
        </div>
    </div>
</template>

<style scoped>
  h1
  {
      text-align: center;
      margin-top: 2%;
  }
  #input
  {
      margin-left: 15%;
      margin-right: 15%;
      text-align: center;
  }
  #Button
  {
      margin-top: 2%;
      margin-bottom: 10%;
      text-align: center;
  }
</style>