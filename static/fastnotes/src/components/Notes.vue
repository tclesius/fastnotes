<script setup>
import NavBar from "./NavBar.vue";
import { useNoteStore } from "../stores/note";
import { storeToRefs } from "pinia";
import { ref } from "vue";

const notesStore = useNoteStore();
const { notes } = storeToRefs(notesStore);

const expandedNoteId = ref();

function toggleCollapsed(id) {
  if (expandedNoteId.value === id) {
    expandedNoteId.value = null;
  } else {
    expandedNoteId.value = id;
  }
}
</script>

<template>
  <NavBar></NavBar>

  <h1>Meine Notizen</h1>
  <hr>
  <div class="container">
    <div class="row">
      <div class="col-md-12" v-for="(note, id) in notes" :key="note.id">
        <b-card style="margin-bottom: 20px; box-shadow: 0 0 0 1px lightgrey; border-radius: 5px;">
          <b-card-title>{{ note.title }}</b-card-title>
          <b-card-text>{{ note.text }}</b-card-text>
          <hr>
          <div id="edit">
            <b-collapse :visible="expandedNoteId === id" class="mt-2">
              <span>Titel</span>
              <b-form-input v-model="note.title" placeholder="Titel eingeben" size="lg" type="text"></b-form-input>
              <span>Text</span>
              <b-form-input v-model="note.text" placeholder="Titel eingeben" size="lg" type="text"></b-form-input>
              <div id="ButtonUpdate">
                <b-button variant="light" @click="notesStore.update(id, { title: note.title, text: note.text })">speichern</b-button>
              </div>
              <hr>
            </b-collapse>
            <b-button id="ButtonEdit" variant="light" @click="toggleCollapsed(id)">bearbeiten</b-button>
            <b-button variant="light" @click="notesStore.remove(id)">löschen</b-button>
          </div>
        </b-card>
      </div>
    </div>
  </div>
</template>


<style scoped>
#ButtonUpdate {
  margin-top: 2%;
  margin-bottom: 2%;
  text-align: center;
}
h1 {
  text-align: center;
  margin-top: 2%;
}
</style>
