<template>
  <div class="w3-container">
    <h3>Filmes:</h3>
    <table class="w3-table-all">
      <thead>
        <tr>
          <th>Título</th>
          <th>Ano</th>
          <th>Classificação</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="r in filmes" 
            v-bind:key="r.id.value"
            @click="goFilme(r.id)"> 
          <td>{{r.titulo}}</td>
          <td>{{r.ano}}</td>
          <td>{{r.classificacao}}</td>
        </tr>
      </tbody>
    </table> 
  </div> 
</template>
<script>
import axios from 'axios';

  export default {
    name: 'Filmes',

    metaInfo: {
      title: 'IMDB da Wish',
    },

    data() {
      return {
            filmes: null,
        };
    },

    created: function() {
      axios
        .get('http://localhost:7001/api/filmes')
        .then(res => {
          this.filmes = res.data;
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