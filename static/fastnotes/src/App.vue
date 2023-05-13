<script setup>
  import { useCounterStore } from './stores/useCounterStore'
  import {storeToRefs} from "pinia";
  import {DefaultService} from "./client";
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
    <!-- Even on the template -->
    <b-button variant="primary" @click="store.increment()">Increment</b-button>
    <h1>{{name}}<b-badge>{{doubleCount}}</b-badge></h1>
</template>

