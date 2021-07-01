<template>
  <ConsultaFilme :idr="$route.params.idFilme" mensagem="Teste"/>
</template>

<script>
import ConsultaFilme from "@/components/ConsultaFilme.vue";

export default {
  components: {
    ConsultaFilme
  }
};
</script>
