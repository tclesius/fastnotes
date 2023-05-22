<!--<script setup>
  import { useCounterStore } from './stores/useCounterStore'
  import {storeToRefs} from "pinia";
  import {DefaultService, NotesService} from "./client";
  import {onMounted} from "@vue/compat";
  // access the `stores` variable anywhere in the component ✨
  const store = useCounterStore()
  // `name` and `doubleCount` are reactive refs
  // This will also extract refs for properties added by plugins
  // but skip any action or non-reactive (non ref/reactive) property
  const { name, doubleCount } = storeToRefs(store)
  // the increment action can just be destructured
  const { increment } = store
  async function check(){
      const healthcheck = await DefaultService.healthcheck()
      console.log(healthcheck);
  }
  onMounted(check)
</script>

<template>
    &lt;!&ndash; Even on the template &ndash;&gt;
    <b-button variant="primary" @click="store.increment()">Increment</b-button>
    <h1>{{name}}<b-badge>{{doubleCount}}</b-badge></h1>
</template>-->

<script setup>
import {DefaultService, NotesService} from "./client";
  import {ref} from "vue";

  const notes = ref([])

  //DefaultService.getNotesNotesGet(0,100).then((response) => response).then((data) => notes.value = data);
  NotesService.getNotes(0,100).then((response) => response).then((data) => notes.value = data);

  function deleteItem(id) {
      //DefaultService.deleteNoteNotesNoteIdDelete(id);
      //DefaultService.getNotesNotesGet(0,100).then((response) => response).then((data) => notes.value = data);
      NotesService.deleteNote(id);
      NotesService.getNotes(0,100).then((response) => response).then((data) => notes.value = data);
  }

  let inputText = "";
  let inputTitle = "";
  function createNote()
  {
      if(inputText.length != 0 || inputTitle.length != 0)
      {
          NotesService.createNote({title: inputTitle, text: inputText});
          NotesService.getNotes(0,100).then((response) => response).then((data) => notes.value = data);
      }
  }
</script>
<template>


    <h1>Notizen App</h1>
    <hr>
<header>
     <b-nav tabs align="center">
      <b-nav-item href="#1">Notiz anlegen</b-nav-item>
      <b-nav-item href="#1">Meine Notizen</b-nav-item>
    </b-nav>
</header>

<div id="input">

<span>Titel eingeben</span>
<p style="white-space: pre-line;">{{inputTitle}}</p>
    <b-form-input v-model="inputTitle" type="text" placeholder="Titel eingeben"
    size="lg"
    ></b-form-input>

<span>Notiz eingeben</span>
    <b-textarea v-model="inputText" type="text" placeholder="Notiz eingeben"
    size="lg"
    >

    </b-textarea>

</div>

<div id="Button">
    <b-button @click="createNote()" variant="primary">Notiz speichern</b-button>
</div>

    <h1>Meine Notizen</h1>
    <hr>

<div id="card">
  <b-card-group rowspan>
  <b-card v-for="note in notes"
  style="min-width: 30rem; margin: 5px; box-shadow: 0px 0px 0px 1px lightgrey; border-radius: 5px;"
  >
   <b-card-title>{{note.title}}</b-card-title>
   <b-card-text>{{note.text}}</b-card-text>
       <hr>
   <div id="edit">
      <b-button href="#1" variant="light" size="sm">bearbeiten</b-button>
      <b-button @click="deleteItem(note.id)" variant="light" size="sm">löschen</b-button>
   </div>
  </b-card>
  </b-card-group>
</div>
</template>

<style scoped>
  header{margin-bottom: 5%}
  h1{text-align: center; margin-top: 2%;}
  #input{margin-left: 15%; margin-right: 15%; text-align: center;}
  #Button{margin-top: 2%; margin-bottom: 10%; text-align: center}
  #card{margin-left: 15%; margin-right: 15%;}
</style>