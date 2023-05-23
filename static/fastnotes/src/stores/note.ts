import {defineStore} from "pinia";
import {ref} from "vue";
import {NoteCreate, NotesService, NoteUpdate} from "../client";


// pessimistic strategy -> UI gets updated after await lock is solved (waiting for API response)
// ! no error handling !
// ! no request status ! ( should be there for displaying loading or so )

export const useNoteStore = defineStore('note', () =>{
    const notes = ref({})
    async function get(id:number) {
        return {id: notes.value[id]}
    }
    async function getPaginated(skip:number, limit:number) {
        const result = await NotesService.getNotes(skip,limit);
        notes.value = {}
        result.map((note) => {
            notes.value[note.id] = {title: note.title, text: note.text}
        })
    }
    async function update(id: number, requestBody: NoteUpdate) {
        const result = await NotesService.updateNote(id, requestBody)
        notes.value[id] = {title: result.title, text: result.text};
    }
    async function remove(id: number){
        await NotesService.deleteNote(id)
        delete notes.value[id]
    }
    async function create(requestBody: NoteCreate){
        const result = await NotesService.createNote(requestBody)
        notes.value[result.id] = {title: result.title, text: result.text}
    }
    async function search(query: string){
        const result = await NotesService.searchNotes(query)
        notes.value = {}
        result.map((note) => {
            notes.value[note.id] = {title: note.title, text: note.text}
        })
    }
    return {notes, get, getPaginated, update, remove, create, search};
})