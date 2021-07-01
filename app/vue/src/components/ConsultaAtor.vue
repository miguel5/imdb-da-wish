<template>
  <div class="w3-container">
    <h1 class="w3-header w3-blue">{{idr}}</h1>
    <ul class="w3-ul w3-border">
      <li><h2>Filmes em que participou</h2></li>
    </ul>
      <ul class="w3-ul w3-hoverable" v-for="dado in dados" :key="dado.id" @click="goFilme(dado.id)">
      <li>{{dado.titulo}}</li>
    </ul>
  </div> 
</template>
<script>
import axios from 'axios';

  export default {
    name: 'Filme',

    props: ["idr", "mensagem"],

    data() {
      return {
            dados: null,
        };
    },

    created: function() {
      axios
        .get('http://localhost:7001/api/filmes/ator/' + this.idr)
        .then(res => {
          this.dados = res.data;
        })
    },

    methods: {
        goFilme: function(id){
            this.$router.push('/filmes/' + id);
        }
    }

  }
</script>
<style>
  h3 {
    margin-bottom: 5%;
  }
</style>