<script setup>
  import {useNoteStore} from "./stores/note";
  import {storeToRefs} from "pinia";
  import {onMounted, ref} from "vue";

  const notesStore = useNoteStore()

  const { notes } = storeToRefs(notesStore)

  const note = ref({title:'',text:''})

  onMounted(() => notesStore.getPaginated(0,100))
</script>
<template>


  <h1>Notizen App</h1>
  <hr>
  <header>
    <b-nav align="center" tabs>
      <b-nav-item href="#1">Notiz anlegen</b-nav-item>
      <b-nav-item href="#1">Meine Notizen</b-nav-item>
    </b-nav>
  </header>

  <div id="input">

    <span>Titel eingeben</span>
    <!-- <p style="white-space: pre-line;">{{ input.title }}</p> -->
    <b-form-input v-model="note.title" placeholder="Titel eingeben" size="lg"
                  type="text">
    </b-form-input>

    <span>Notiz eingeben</span>
    <b-textarea v-model="note.text" placeholder="Notiz eingeben" size="lg"
                type="text">
    </b-textarea>

  </div>

  <div id="Button">
    <b-button variant="primary" @click="notesStore.create(note)">Notiz speichern</b-button>
  </div>

  <h1>Meine Notizen</h1>
  <hr>

  <div id="card">
    <b-card-group rowspan>
      <b-card v-for="(note, id) in notes"
              style="min-width: 30rem; margin: 5px; box-shadow: 0 0 0 1px lightgrey; border-radius: 5px;">
        <b-card-title>{{ note.title }}</b-card-title>
        <b-card-text>{{ note.text }}</b-card-text>
        <hr>
        <div id="edit">
          <b-button href="#1" size="sm" variant="light">bearbeiten</b-button>
          <b-button size="sm" variant="light" @click="notesStore.remove(id)">löschen</b-button>
        </div>
      </b-card>
    </b-card-group>
  </div>
</template>

<style scoped>
header {
  margin-bottom: 5%
}

h1 {
  text-align: center;
  margin-top: 2%;
}

#input {
  margin-left: 15%;
  margin-right: 15%;
  text-align: center;
}

#Button {
  margin-top: 2%;
  margin-bottom: 10%;
  text-align: center
}

#card {
  margin-left: 15%;
  margin-right: 15%;
}
</style>