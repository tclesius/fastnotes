<script setup>
  import {useNoteStore} from "./stores/note";
  import {storeToRefs} from "pinia";
  import {onMounted, ref} from "vue";

  const notesStore = useNoteStore() //Konstruktor für die "Klasse" notesStore

  const { notes } = storeToRefs(notesStore) //Array mit allen Notes, welche im Notestore gespeichert sind

  const note = ref({title:'',text:''}) //Temporärer Speicher für Input-Daten --> Zur Erstellung von Notizen

  onMounted(() => notesStore.getPaginated(0,100)) //Initiales Laden von Daten aus dem Server --> Notestore wird mit Daten gefüllt
</script>
<template>
  <router-view></router-view>
</template>

<style scoped>
header {
  margin-bottom: 5%
}

h1 {
  text-align: center;
  margin-top: 2%;
}
</style>