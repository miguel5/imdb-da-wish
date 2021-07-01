<template>
  <div class="w3-container">
    <h3>Atores:</h3>
    <table class="w3-table-all">
      <thead>
        <tr>
          <th>Nome</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="ator in atores" v-bind:key="ator.nome" @click="goAtor(ator.id)"> 
          <td>{{ator.nome}}</td>
        </tr>
      </tbody>
    </table> 
  </div> 
</template>
<script>
import axios from 'axios';

  export default {
    name: 'Atores',

    data() {
      return {
            atores: null,
        };
    },

    created: function() {
      axios
        .get('http://localhost:7001/api/atores')
        .then(res => {
          this.atores = res.data;
        })
    },

    methods: {
        goAtor: function(id){
            this.$router.push('/atores/' + id);
        }
    }
  }
</script>
<style>
  h3 {
    margin-bottom: 5%;
  }
</style>