<template>
  <div class="w3-container">
    <h2 class="w3-header w3-blue">{{dados[0].titulo}}</h2>
    <table class="w3-table-all">
        <tr>
            <th>Ano</th><th>País</th><th>Duração</th><th>Classificação</th><th>Linguagem</th><th>Diretor</th><th>Género</th>
        </tr>
        <tr v-for="dado in dados" :key="dado.titulo">
            <td>{{dado.ano}}</td><td>{{dado.pais}}</td><td>{{dado.duracao}}</td><td>{{dado.classificacao}}</td><td>{{dado.linguagem}}</td>
            <td>{{dado.diretor}}</td><td>{{dado.genero}}</td>
        </tr>
    </table>
    <p>{{dados[0].descricao}}</p>
    <ul class="w3-ul w3-border">
      <li><h2>Atores</h2></li>
    </ul>
      <ul class="w3-ul w3-hoverable" v-for="ator in atores" :key="ator.id" @click="goAtor(ator.id)">
      <li>{{ator.nome}}</li>
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
            atores: null,
        };
    },

    created: function() {
      axios
        .get('http://localhost:7001/api/filmes/filme/' + this.idr)
        .then(res => {
          this.dados = res.data;
        })

      axios
        .get('http://localhost:7001/api/atores/filme/' + this.idr)
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