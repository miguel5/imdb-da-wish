<template>
  <ConsultaAtor :idr="$route.params.idAtor"/>
</template>

<script>
import ConsultaAtor from "@/components/ConsultaAtor.vue";

export default {
  components: {
    ConsultaAtor
  }
};
</script>